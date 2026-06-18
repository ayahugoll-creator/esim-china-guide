#!/bin/bash
# Pull analytics from Cloudflare API.
# Requires: .env file with CLOUDFLARE_API_TOKEN and CLOUDFLARE_ZONE_ID
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# Load credentials
if [ -f "$PROJECT_DIR/.env" ]; then
  source "$PROJECT_DIR/.env"
fi

API_TOKEN="${CLOUDFLARE_API_TOKEN:-}"
ZONE_ID="${CLOUDFLARE_ZONE_ID:-}"

if [ -z "$API_TOKEN" ] || [ -z "$ZONE_ID" ]; then
  echo "Error: Set CLOUDFLARE_API_TOKEN and CLOUDFLARE_ZONE_ID in .env"
  exit 1
fi

CF_API="https://api.cloudflare.com/client/v4"
AUTH_HEADER="Authorization: Bearer $API_TOKEN"

# === Helpers ===
cf_rest() {
  local method="$1" path="$2"
  curl -s -X "$method" "$CF_API$path" -H "$AUTH_HEADER" -H "Content-Type: application/json"
}

cf_graphql() {
  local query="$1"
  curl -s -X POST "https://api.cloudflare.com/client/v4/graphql" \
    -H "$AUTH_HEADER" \
    -H "Content-Type: application/json" \
    -d "{\"query\": $(echo "$query" | jq -Rs .)}"
}

# === 1. Zone overview ===
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📊 Zone Overview (last 24h)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

NOW=$(date -u +%Y-%m-%dT%H:%M:%SZ)
YESTERDAY=$(date -u -v-1d +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || date -u -d "1 day ago" +%Y-%m-%dT%H:%M:%SZ)

QUERY='{
  viewer {
    zones(filter: {zoneTag: "'$ZONE_ID'"}) {
      httpRequests1hGroups(
        filter: {datetime_geq: "'$YESTERDAY'", datetime_lt: "'$NOW'"},
        limit: 5,
        orderBy: [datetime_DESC]
      ) {
        dimensions { datetime }
        sum { requests pageViews bytes }
        avg { sampleInterval }
      }
    }
  }
}'

cf_graphql "$QUERY" | jq -r '
  .data.viewer.zones[0].httpRequests1hGroups[] |
  "  \(.dimensions.datetime) | Req: \(.sum.requests) | Views: \(.sum.pageViews) | MB: \((.sum.bytes / 1048576 * 100 | round) / 100)"
' 2>/dev/null || echo "  (GraphQL query returned no data or failed)"

echo ""

# === 2. Top pages ===
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📄 Top Pages (last 7 days)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

WEEK_AGO=$(date -u -v-7d +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || date -u -d "7 days ago" +%Y-%m-%dT%H:%M:%SZ)

QUERY='{
  viewer {
    zones(filter: {zoneTag: "'$ZONE_ID'"}) {
      httpRequests1hGroups(
        filter: {datetime_geq: "'$WEEK_AGO'", datetime_lt: "'$NOW'"},
        limit: 20,
        orderBy: [sum_pageViews_DESC]
      ) {
        dimensions { clientRequestPath }
        sum { pageViews requests }
      }
    }
  }
}'

cf_graphql "$QUERY" | jq -r '
  .data.viewer.zones[0].httpRequests1hGroups[] |
  "  \(.sum.pageViews) views — \(.dimensions.clientRequestPath)"
' 2>/dev/null | sort -rn | head -15

echo ""

# === 3. AI Bot traffic ===
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🤖 AI Bot Requests (last 7 days)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# List of known AI bot user agents to check
AI_BOTS=(
  "GPTBot"
  "ChatGPT-User"
  "ClaudeBot"
  "anthropic"
  "PerplexityBot"
  "Applebot"
  "Bytespider"
  "CCBot"
  "BingBot"
)

QUERY='{
  viewer {
    zones(filter: {zoneTag: "'$ZONE_ID'"}) {
      httpRequests1hGroups(
        filter: {datetime_geq: "'$WEEK_AGO'", datetime_lt: "'$NOW'"},
        limit: 10000
      ) {
        dimensions { clientRequestPath userAgent }
        sum { requests }
      }
    }
  }
}'

cf_graphql "$QUERY" | jq -r '
  .data.viewer.zones[0].httpRequests1hGroups[]
  | select(.dimensions.userAgent != null)
  | "\(.dimensions.userAgent)|\(.sum.requests)|\(.dimensions.clientRequestPath)"
' 2>/dev/null | while IFS='|' read -r ua reqs path; do
  for bot in "${AI_BOTS[@]}"; do
    if [[ "$ua" == *"$bot"* ]]; then
      echo "  $bot: $reqs req → $path"
    fi
  done
done | sort | uniq -c | sort -rn | head -20

echo ""

# === 4. Planner endpoint hits ===
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🎯 Planner Submissions — /api/planner-event (last 7 days)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

QUERY='{
  viewer {
    zones(filter: {zoneTag: "'$ZONE_ID'"}) {
      httpRequests1hGroups(
        filter: {
          datetime_geq: "'$WEEK_AGO'",
          datetime_lt: "'$NOW'",
          clientRequestPath: "/api/planner-event"
        },
        limit: 1000
      ) {
        sum { requests }
        dimensions { datetime }
      }
    }
  }
}'

TOTAL=$(cf_graphql "$QUERY" | jq -r '
  [.data.viewer.zones[0].httpRequests1hGroups[]?.sum.requests // 0] | add
' 2>/dev/null)

echo "  Total submissions: ${TOTAL:-0}"

# Daily breakdown
cf_graphql "$QUERY" | jq -r '
  .data.viewer.zones[0].httpRequests1hGroups[]
  | "  \(.dimensions.datetime) — \(.sum.requests) submissions"
' 2>/dev/null | sort -r | head -10

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Done. Run again: ./scripts/pull-analytics.sh"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
