#!/bin/bash
# Pull analytics from Cloudflare GraphQL API.
# Requires: .env file with CLOUDFLARE_API_TOKEN and CLOUDFLARE_ZONE_ID
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

if [ -f "$PROJECT_DIR/.env" ]; then
  source "$PROJECT_DIR/.env"
fi

API_TOKEN="${CLOUDFLARE_API_TOKEN:-}"
ZONE_ID="${CLOUDFLARE_ZONE_ID:-}"

if [ -z "$API_TOKEN" ] || [ -z "$ZONE_ID" ]; then
  echo "Error: Set CLOUDFLARE_API_TOKEN and CLOUDFLARE_ZONE_ID in .env"
  exit 1
fi

AUTH="Authorization: Bearer $API_TOKEN"
URL="https://api.cloudflare.com/client/v4/graphql"

ql() {
  curl -s -X POST "$URL" -H "$AUTH" -H "Content-Type: application/json" \
    -d "{\"query\": $(echo "$1" | jq -Rs .)}"
}

NOW=$(date -u +%Y-%m-%dT%H:%M:%SZ)
DAY_AGO=$(date -u -v-1d +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || date -u -d "1 day ago" +%Y-%m-%dT%H:%M:%SZ)
TODAY=$(date -u +%Y-%m-%d)
WEEK_AGO=$(date -u -v-7d +%Y-%m-%d 2>/dev/null || date -u -d "7 days ago" +%Y-%m-%d)

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  esimchina.trade — Cloudflare Analytics"
echo "  $(date '+%Y-%m-%d %H:%M')"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# === Hourly traffic (last 24h) ===
echo "📊 Hourly — Last 24h"
echo ""

ql '{
  viewer {
    zones(filter: {zoneTag: "'$ZONE_ID'"}) {
      httpRequests1hGroups(
        filter: {datetime_geq: "'$DAY_AGO'", datetime_lt: "'$NOW'"},
        limit: 24,
        orderBy: [datetime_DESC]
      ) {
        dimensions { datetime }
        sum { requests pageViews bytes }
      }
    }
  }
}' | jq -r '
  (.data.viewer.zones[0].httpRequests1hGroups // [])[]
  | "  \(.dimensions.datetime)  req:\(.sum.requests)  views:\(.sum.pageViews)  mb:\((.sum.bytes / 1048576 * 100 | round) / 100)"
' 2>/dev/null || echo "  (no data)"

echo ""

# === Daily traffic (last 7 days) ===
echo "📊 Daily — Last 7 Days"
echo ""

ql '{
  viewer {
    zones(filter: {zoneTag: "'$ZONE_ID'"}) {
      httpRequests1dGroups(
        filter: {date_geq: "'$WEEK_AGO'", date_lt: "'$TODAY'"},
        limit: 7,
        orderBy: [date_DESC]
      ) {
        dimensions { date }
        sum { requests pageViews bytes }
        uniq { uniques }
      }
    }
  }
}' | jq -r '
  (.data.viewer.zones[0].httpRequests1dGroups // [])[]
  | "  \(.dimensions.date)  req:\(.sum.requests)  views:\(.sum.pageViews)  unique:\(.uniq.uniques)  mb:\((.sum.bytes / 1048576 * 100 | round) / 100)"
' 2>/dev/null || echo "  (no data)"

echo ""

# === 7-day totals ===
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  7-Day Totals"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

ql '{
  viewer {
    zones(filter: {zoneTag: "'$ZONE_ID'"}) {
      httpRequests1dGroups(
        filter: {date_geq: "'$WEEK_AGO'", date_lt: "'$TODAY'"},
        limit: 7
      ) {
        sum { requests pageViews bytes }
        uniq { uniques }
      }
    }
  }
}' | jq -r '
  (.data.viewer.zones[0].httpRequests1dGroups // []) as $d |
  "  Requests:     \(( [$d[].sum.requests] | add) // 0 )",
  "  Page views:   \(( [$d[].sum.pageViews] | add) // 0 )",
  "  Uniques:      \(( [$d[].uniq.uniques] | add) // 0 )",
  "  Bandwidth:    \(( (([$d[].sum.bytes] | add) // 0) / 1048576 * 100 | round) / 100 ) MB"
' 2>/dev/null

echo ""
echo "  Planner uses:  0 (just deployed)"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
