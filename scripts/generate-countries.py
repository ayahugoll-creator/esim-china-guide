#!/usr/bin/env python3
"""Generate Hugo country pages for China entry requirements."""

import os

OUTPUT_DIR = "../content/countries"

COUNTRIES = [
    # === 30-Day Unilateral Visa-Free ===
    # Europe
    {"name": "France", "status": "visa-free", "flag": "🇫🇷", "region": "Europe",
     "policy": "French citizens can enter China without a visa for up to 30 days. Part of China's unilateral visa-free policy covering all EU countries. Valid until December 31, 2026.",
     "notes": "France was in the first batch of European countries granted visa-free access in November 2023."},
    {"name": "Italy", "status": "visa-free", "flag": "🇮🇹", "region": "Europe",
     "policy": "Italian citizens can enter China without a visa for up to 30 days for tourism, business, or family visits. Valid until December 31, 2026."},
    {"name": "Spain", "status": "visa-free", "flag": "🇪🇸", "region": "Europe",
     "policy": "Spanish citizens can enter China without a visa for up to 30 days. Part of China's unilateral visa-free policy. Valid until December 31, 2026."},
    {"name": "Netherlands", "status": "visa-free", "flag": "🇳🇱", "region": "Europe",
     "policy": "Dutch citizens can enter China without a visa for up to 30 days. Valid until December 31, 2026."},
    {"name": "Switzerland", "status": "visa-free", "flag": "🇨🇭", "region": "Europe",
     "policy": "Swiss citizens can enter China without a visa for up to 30 days. Valid until December 31, 2026."},
    {"name": "Sweden", "status": "visa-free", "flag": "🇸🇪", "region": "Europe",
     "policy": "Swedish citizens can enter China without a visa for up to 30 days. Valid until December 31, 2026."},
    {"name": "Norway", "status": "visa-free", "flag": "🇳🇴", "region": "Europe",
     "policy": "Norwegian citizens can enter China without a visa for up to 30 days. Valid until December 31, 2026."},
    {"name": "Denmark", "status": "visa-free", "flag": "🇩🇰", "region": "Europe",
     "policy": "Danish citizens can enter China without a visa for up to 30 days. Valid until December 31, 2026."},
    {"name": "Finland", "status": "visa-free", "flag": "🇫🇮", "region": "Europe",
     "policy": "Finnish citizens can enter China without a visa for up to 30 days. Valid until December 31, 2026."},
    {"name": "Austria", "status": "visa-free", "flag": "🇦🇹", "region": "Europe",
     "policy": "Austrian citizens can enter China without a visa for up to 30 days. Valid until December 31, 2026."},
    {"name": "Belgium", "status": "visa-free", "flag": "🇧🇪", "region": "Europe",
     "policy": "Belgian citizens can enter China without a visa for up to 30 days. Valid until December 31, 2026."},
    {"name": "Portugal", "status": "visa-free", "flag": "🇵🇹", "region": "Europe",
     "policy": "Portuguese citizens can enter China without a visa for up to 30 days. Valid until December 31, 2026."},
    {"name": "Greece", "status": "visa-free", "flag": "🇬🇷", "region": "Europe",
     "policy": "Greek citizens can enter China without a visa for up to 30 days. Valid until December 31, 2026."},
    {"name": "Ireland", "status": "visa-free", "flag": "🇮🇪", "region": "Europe",
     "policy": "Irish citizens can enter China without a visa for up to 30 days. Valid until December 31, 2026."},
    {"name": "Poland", "status": "visa-free", "flag": "🇵🇱", "region": "Europe",
     "policy": "Polish citizens can enter China without a visa for up to 30 days. Valid until December 31, 2026."},
    {"name": "Czech Republic", "status": "visa-free", "flag": "🇨🇿", "region": "Europe",
     "policy": "Czech citizens can enter China without a visa for up to 30 days. Part of the EU-wide unilateral visa-free policy. Valid until December 31, 2026."},
    {"name": "Hungary", "status": "visa-free", "flag": "🇭🇺", "region": "Europe",
     "policy": "Hungarian citizens can enter China without a visa for up to 30 days. Valid until December 31, 2026."},
    {"name": "Romania", "status": "visa-free", "flag": "🇷🇴", "region": "Europe",
     "policy": "Romanian citizens can enter China without a visa for up to 30 days. Valid until December 31, 2026."},
    {"name": "Croatia", "status": "visa-free", "flag": "🇭🇷", "region": "Europe",
     "policy": "Croatian citizens can enter China without a visa for up to 30 days. Valid until December 31, 2026."},
    {"name": "Slovakia", "status": "visa-free", "flag": "🇸🇰", "region": "Europe",
     "policy": "Slovak citizens can enter China without a visa for up to 30 days. Valid until December 31, 2026."},
    {"name": "Slovenia", "status": "visa-free", "flag": "🇸🇮", "region": "Europe",
     "policy": "Slovenian citizens can enter China without a visa for up to 30 days. Valid until December 31, 2026."},
    {"name": "Bulgaria", "status": "visa-free", "flag": "🇧🇬", "region": "Europe",
     "policy": "Bulgarian citizens can enter China without a visa for up to 30 days. Valid until December 31, 2026."},
    {"name": "Estonia", "status": "visa-free", "flag": "🇪🇪", "region": "Europe",
     "policy": "Estonian citizens can enter China without a visa for up to 30 days. Valid until December 31, 2026."},
    {"name": "Latvia", "status": "visa-free", "flag": "🇱🇻", "region": "Europe",
     "policy": "Latvian citizens can enter China without a visa for up to 30 days. Valid until December 31, 2026."},
    {"name": "Lithuania", "status": "visa-free", "flag": "🇱🇹", "region": "Europe",
     "policy": "Lithuanian citizens can enter China without a visa for up to 30 days. Valid until December 31, 2026."},
    {"name": "Luxembourg", "status": "visa-free", "flag": "🇱🇺", "region": "Europe",
     "policy": "Luxembourg citizens can enter China without a visa for up to 30 days. Valid until December 31, 2026."},
    {"name": "Malta", "status": "visa-free", "flag": "🇲🇹", "region": "Europe",
     "policy": "Maltese citizens can enter China without a visa for up to 30 days. Valid until December 31, 2026."},
    {"name": "Iceland", "status": "visa-free", "flag": "🇮🇸", "region": "Europe",
     "policy": "Icelandic citizens can enter China without a visa for up to 30 days. Valid until December 31, 2026."},
    {"name": "Monaco", "status": "visa-free", "flag": "🇲🇨", "region": "Europe",
     "policy": "Monegasque citizens can enter China without a visa for up to 30 days. Valid until December 31, 2026."},
    {"name": "Liechtenstein", "status": "visa-free", "flag": "🇱🇮", "region": "Europe",
     "policy": "Liechtenstein citizens can enter China without a visa for up to 30 days. Valid until December 31, 2026."},
    {"name": "Andorra", "status": "visa-free", "flag": "🇦🇩", "region": "Europe",
     "policy": "Andorran citizens can enter China without a visa for up to 30 days. Valid until December 31, 2026."},
    {"name": "Montenegro", "status": "visa-free", "flag": "🇲🇪", "region": "Europe",
     "policy": "Montenegrin citizens can enter China without a visa for up to 30 days. Valid until December 31, 2026."},
    {"name": "North Macedonia", "status": "visa-free", "flag": "🇲🇰", "region": "Europe",
     "policy": "North Macedonian citizens can enter China without a visa for up to 30 days. Valid until December 31, 2026."},
    {"name": "Cyprus", "status": "visa-free", "flag": "🇨🇾", "region": "Europe",
     "policy": "Cypriot citizens can enter China without a visa for up to 30 days. Valid until December 31, 2026."},

    # Asia
    {"name": "Japan", "status": "visa-free", "flag": "🇯🇵", "region": "Asia",
     "policy": "Japanese citizens can enter China without a visa for up to 30 days. Part of China's unilateral visa-free policy. Valid until December 31, 2026.",
     "notes": "Japan was a late but significant addition to the visa-free list. Massive inbound tourism from Japan since the policy started."},
    {"name": "South Korea", "status": "visa-free", "flag": "🇰🇷", "region": "Asia",
     "policy": "South Korean citizens can enter China without a visa for up to 30 days. Part of China's unilateral visa-free policy. Valid until December 31, 2026.",
     "notes": "2.66 million Korean visitors in Q1 2026 alone — the largest single source market."},
    {"name": "Brunei", "status": "visa-free", "flag": "🇧🇳", "region": "Asia",
     "policy": "Bruneian citizens can enter China without a visa for up to 30 days. Valid until December 31, 2026."},
    {"name": "Bahrain", "status": "visa-free", "flag": "🇧🇭", "region": "Asia",
     "policy": "Bahraini citizens can enter China without a visa for up to 30 days. Valid until December 31, 2026."},
    {"name": "Kuwait", "status": "visa-free", "flag": "🇰🇼", "region": "Asia",
     "policy": "Kuwaiti citizens can enter China without a visa for up to 30 days. Valid until December 31, 2026."},
    {"name": "Oman", "status": "visa-free", "flag": "🇴🇲", "region": "Asia",
     "policy": "Omani citizens can enter China without a visa for up to 30 days. Valid until December 31, 2026."},
    {"name": "Saudi Arabia", "status": "visa-free", "flag": "🇸🇦", "region": "Asia",
     "policy": "Saudi Arabian citizens can enter China without a visa for up to 30 days. Valid until December 31, 2026.",
     "notes": "Middle East is the fastest-growing source region for China tourism, with over 100% growth."},

    # Americas
    {"name": "Canada", "status": "visa-free", "flag": "🇨🇦", "region": "Americas",
     "policy": "Canadian citizens can enter China without a visa for up to 30 days. Added to the visa-free list on February 17, 2026. Valid until December 31, 2026.",
     "notes": "Canada was added the same day as the UK — one of the most significant recent expansions."},
    {"name": "Brazil", "status": "visa-free", "flag": "🇧🇷", "region": "Americas",
     "policy": "Brazilian citizens can enter China without a visa for up to 30 days. Part of the South America pilot program. Valid until December 31, 2026.",
     "notes": "Brazil is part of a South America visa-free pilot that saw 50.5% growth in arrivals."},
    {"name": "Argentina", "status": "visa-free", "flag": "🇦🇷", "region": "Americas",
     "policy": "Argentine citizens can enter China without a visa for up to 30 days. Part of the South America pilot. Valid until December 31, 2026."},
    {"name": "Chile", "status": "visa-free", "flag": "🇨🇱", "region": "Americas",
     "policy": "Chilean citizens can enter China without a visa for up to 30 days. Part of the South America pilot. Valid until December 31, 2026."},
    {"name": "Peru", "status": "visa-free", "flag": "🇵🇪", "region": "Americas",
     "policy": "Peruvian citizens can enter China without a visa for up to 30 days. Part of the South America pilot. Valid until December 31, 2026."},
    {"name": "Uruguay", "status": "visa-free", "flag": "🇺🇾", "region": "Americas",
     "policy": "Uruguayan citizens can enter China without a visa for up to 30 days. Part of the South America pilot. Valid until December 31, 2026."},

    # Oceania
    {"name": "New Zealand", "status": "visa-free", "flag": "🇳🇿", "region": "Oceania",
     "policy": "New Zealand citizens can enter China without a visa for up to 30 days. Part of China's unilateral visa-free policy. Valid until December 31, 2026."},

    # Russia (special case)
    {"name": "Russia", "status": "visa-free", "flag": "🇷🇺", "region": "Europe/Asia",
     "policy": "Russian citizens can enter China without a visa for up to 30 days. Valid from September 15, 2025 to September 14, 2026.",
     "notes": "Russia has a different validity period from other countries. Over 318,000 Russian entries via Shanghai alone (up 67.8% YoY)."},

    # === Mutual Visa Exemption ===
    {"name": "Thailand", "status": "visa-free", "flag": "🇹🇭", "region": "Asia",
     "policy": "Thai citizens can enter China without a visa for up to 30 days under a mutual visa exemption agreement. Cumulative stay cannot exceed 90 days within any 180-day period."},
    {"name": "Singapore", "status": "visa-free", "flag": "🇸🇬", "region": "Asia",
     "policy": "Singaporean citizens can enter China without a visa for up to 30 days under a mutual visa exemption agreement."},
    {"name": "Malaysia", "status": "visa-free", "flag": "🇲🇾", "region": "Asia",
     "policy": "Malaysian citizens can enter China without a visa for up to 30 days under a mutual visa exemption agreement. Malaysia is now the 3rd largest source market for China tourism."},
    {"name": "UAE", "status": "visa-free", "flag": "🇦🇪", "region": "Asia",
     "policy": "UAE citizens can enter China without a visa for up to 30 days under a mutual visa exemption agreement."},
    {"name": "Qatar", "status": "visa-free", "flag": "🇶🇦", "region": "Asia",
     "policy": "Qatari citizens can enter China without a visa for up to 30 days under a mutual visa exemption agreement."},
    {"name": "Kazakhstan", "status": "visa-free", "flag": "🇰🇿", "region": "Asia",
     "policy": "Kazakh citizens can enter China without a visa for up to 30 days under a mutual visa exemption agreement."},
    {"name": "Uzbekistan", "status": "visa-free", "flag": "🇺🇿", "region": "Asia",
     "policy": "Uzbek citizens can enter China without a visa for up to 30 days. Cumulative stay cannot exceed 90 days within any 180-day period."},
    {"name": "Georgia", "status": "visa-free", "flag": "🇬🇪", "region": "Asia/Europe",
     "policy": "Georgian citizens can enter China without a visa for up to 30 days. Cumulative stay cannot exceed 90 days within any 180-day period."},
    {"name": "Azerbaijan", "status": "visa-free", "flag": "🇦🇿", "region": "Asia/Europe",
     "policy": "Azerbaijani citizens can enter China without a visa for up to 30 days. Cumulative stay cannot exceed 90 days within any 180-day period."},
    {"name": "Armenia", "status": "visa-free", "flag": "🇦🇲", "region": "Asia/Europe",
     "policy": "Armenian citizens can enter China without a visa for up to 30 days under a mutual visa exemption agreement."},
    {"name": "Maldives", "status": "visa-free", "flag": "🇲🇻", "region": "Asia",
     "policy": "Maldivian citizens can enter China without a visa for up to 30 days under a mutual visa exemption agreement."},

    {"name": "Serbia", "status": "visa-free", "flag": "🇷🇸", "region": "Europe",
     "policy": "Serbian citizens can enter China without a visa for up to 30 days under a mutual visa exemption agreement."},
    {"name": "Albania", "status": "visa-free", "flag": "🇦🇱", "region": "Europe",
     "policy": "Albanian citizens can enter China without a visa for up to 30 days under a mutual visa exemption agreement."},
    {"name": "Bosnia and Herzegovina", "status": "visa-free", "flag": "🇧🇦", "region": "Europe",
     "policy": "Bosnian citizens can enter China without a visa for up to 30 days under a mutual visa exemption agreement."},
    {"name": "Belarus", "status": "visa-free", "flag": "🇧🇾", "region": "Europe",
     "policy": "Belarusian citizens can enter China without a visa for up to 30 days under a mutual visa exemption agreement."},

    {"name": "Ecuador", "status": "visa-free", "flag": "🇪🇨", "region": "Americas",
     "policy": "Ecuadorian citizens can enter China without a visa for up to 30 days under a mutual visa exemption agreement."},
    {"name": "Suriname", "status": "visa-free", "flag": "🇸🇷", "region": "Americas",
     "policy": "Surinamese citizens can enter China without a visa for up to 30 days under a mutual visa exemption agreement."},
    {"name": "Barbados", "status": "visa-free", "flag": "🇧🇧", "region": "Caribbean",
     "policy": "Barbadian citizens can enter China without a visa for up to 30 days under a mutual visa exemption agreement."},
    {"name": "Bahamas", "status": "visa-free", "flag": "🇧🇸", "region": "Caribbean",
     "policy": "Bahamian citizens can enter China without a visa for up to 30 days under a mutual visa exemption agreement."},

    {"name": "Fiji", "status": "visa-free", "flag": "🇫🇯", "region": "Oceania",
     "policy": "Fijian citizens can enter China without a visa for up to 30 days under a mutual visa exemption agreement."},

    {"name": "Seychelles", "status": "visa-free", "flag": "🇸🇨", "region": "Africa",
     "policy": "Seychellois citizens can enter China without a visa for up to 30 days under a mutual visa exemption agreement."},

    # === 240h Transit Only (NOT visa-free) ===
    {"name": "Mexico", "status": "transit", "flag": "🇲🇽", "region": "Americas",
     "policy": "Mexican citizens are NOT eligible for 30-day visa-free entry, but CAN use the 240-hour (10-day) transit visa-free program when flying through China to a third country."},
    {"name": "Indonesia", "status": "transit", "flag": "🇮🇩", "region": "Asia",
     "policy": "Indonesian citizens are NOT eligible for 30-day visa-free entry, but CAN use the 240-hour transit program. For direct visits, an L tourist visa is required."},
    {"name": "Turkey", "status": "transit", "flag": "🇹🇷", "region": "Asia/Europe",
     "policy": "Turkish citizens are NOT eligible for 30-day visa-free entry, but CAN use the 240-hour transit program. For direct visits, apply for an L tourist visa."},

    # === Visa Required (major countries) ===
    {"name": "Philippines", "status": "visa-required", "flag": "🇵🇭", "region": "Asia",
     "policy": "Philippine citizens currently need a visa to enter China. Not included in any visa-free program. Apply for an L tourist visa at the Chinese embassy in Manila, Cebu, or Davao."},
    {"name": "Vietnam", "status": "visa-required", "flag": "🇻🇳", "region": "Asia",
     "policy": "Vietnamese citizens currently need a visa to enter China. Not included in any visa-free program. Apply at the Chinese embassy in Hanoi or consulate in Ho Chi Minh City."},
    {"name": "Pakistan", "status": "visa-required", "flag": "🇵🇰", "region": "Asia",
     "policy": "Pakistani citizens currently need a visa to enter China. Not included in any visa-free program. Apply at the Chinese embassy in Islamabad or consulate in Karachi."},
    {"name": "Bangladesh", "status": "visa-required", "flag": "🇧🇩", "region": "Asia",
     "policy": "Bangladeshi citizens currently need a visa to enter China. Not included in any visa-free program."},
    {"name": "South Africa", "status": "visa-required", "flag": "🇿🇦", "region": "Africa",
     "policy": "South African citizens currently need a visa to enter China. Not included in any visa-free program. Apply at the Chinese embassy in Pretoria or consulates in Cape Town, Johannesburg, or Durban."},
    {"name": "Nigeria", "status": "visa-required", "flag": "🇳🇬", "region": "Africa",
     "policy": "Nigerian citizens currently need a visa to enter China. Not included in any visa-free program."},
    {"name": "Egypt", "status": "visa-required", "flag": "🇪🇬", "region": "Africa",
     "policy": "Egyptian citizens currently need a visa to enter China. Not included in any visa-free program. Apply at the Chinese embassy in Cairo."},
    {"name": "Kenya", "status": "visa-required", "flag": "🇰🇪", "region": "Africa",
     "policy": "Kenyan citizens currently need a visa to enter China. Not included in any visa-free program."},
    {"name": "Iran", "status": "visa-required", "flag": "🇮🇷", "region": "Asia",
     "policy": "Iranian citizens currently need a visa to enter China. Not included in any visa-free program."},
]

TEMPLATE = """---
title: "{name}"
date: 2026-06-04
draft: false
status: "{status}"
flag: "{flag}"
region: "{region}"
policy_summary: "{policy}"
last_verified: "2026-06-04"
source_url: "https://www.nia.gov.cn/"
source_label: "NIA China"
requirements:
  - "Passport valid for at least 3 months from date of entry"
  - "Return or onward ticket recommended"
  - "Not permitted: work, study, journalism, religious activities"
  - "Maximum 30 days per visit"
---

## {name} → China: Entry Requirements 2026

{{{{< status_banner >}}}}

{notes}

### Before You Fly

1. **eSIM first:** Install your China eSIM before departure. QR codes may not load behind the Great Firewall. [Compare China eSIMs →](/posts/best-esim-for-china-travel/)
2. **Alipay setup:** Takes 10 minutes at home. Link your bank card before you fly. [Alipay setup guide →](/posts/alipay-foreigner-setup-guide/)
3. **Do you need a Chinese phone number?** Probably not. [Read our guide →](/posts/chinese-phone-number-foreigner/)

📌 **Source:** [NIA China](https://www.nia.gov.cn/) · Last verified: **2026-06-04**

⚠️ This is not legal advice. Visa policies change. Always confirm with your local Chinese embassy before booking.
"""

TRANSIT_TEMPLATE = """---
title: "{name}"
date: 2026-06-04
draft: false
status: "transit"
flag: "{flag}"
region: "{region}"
policy_summary: "{policy}"
last_verified: "2026-06-04"
source_url: "https://www.nia.gov.cn/"
source_label: "NIA China"
requirements:
  - "Passport valid for at least 3 months"
  - "Confirmed onward ticket to a THIRD country (not back to {name})"
  - "Enter and exit through designated ports (60+ ports in 24 provinces)"
  - "Maximum 240 hours (10 days)"
  - "Must stay within approved regions"
transit_ports:
  - "Beijing (Capital & Daxing)"
  - "Shanghai (Pudong & Hongqiao)"
  - "Guangzhou (Baiyun)"
  - "Shenzhen (Baoan, Shekou)"
  - "Chengdu, Chongqing, Xi'an, Kunming, Hangzhou, Xiamen, and 50+ more"
---

## {name} → China: Entry Requirements 2026

{notes}

**Short version:** {name} citizens are NOT on China's 30-day visa-free list, but CAN use the 240-hour (10-day) transit visa-free program if flying through China to a third country.

**The trick:** Book a multi-city itinerary: {name} → Beijing (stay 5 days) → Tokyo/Seoul/Bangkok (onward). Your transit visa-free is valid for 10 days.

### Before You Fly

1. **eSIM first:** Install your China eSIM before departure. [Compare China eSIMs →](/posts/best-esim-for-china-travel/)
2. **Alipay setup:** Link your bank card before you fly. [Alipay setup guide →](/posts/alipay-foreigner-setup-guide/)
3. **Do you need a Chinese phone number?** [Read our guide →](/posts/chinese-phone-number-foreigner/)

📌 **Source:** [NIA China](https://www.nia.gov.cn/) · Last verified: **2026-06-04**

⚠️ This is not legal advice. Visa policies change. Always confirm with your local Chinese embassy before booking.
"""

VISA_REQUIRED_TEMPLATE = """---
title: "{name}"
date: 2026-06-04
draft: false
status: "visa-required"
flag: "{flag}"
region: "{region}"
policy_summary: "{policy}"
last_verified: "2026-06-04"
source_url: "https://www.nia.gov.cn/"
source_label: "NIA China"
requirements:
  - "Valid passport with at least 6 months validity and 2 blank pages"
  - "Completed visa application form"
  - "Recent passport-size photo"
  - "Travel itinerary (flight + hotel bookings)"
  - "Processing time: typically 4-7 business days"
---

## {name} → China: Entry Requirements 2026

{notes}

### How to Apply for a China Visa

1. Fill the online application at the [Chinese Visa Application Service Center](https://www.visaforchina.cn/)
2. Book an appointment at the nearest Chinese embassy or consulate
3. Bring passport + application + photo + itinerary
4. Pay the visa fee
5. Pick up passport in 4-7 business days

### While You Wait

Prepare everything else while your visa processes:

1. **eSIM:** [Compare China eSIMs →](/posts/best-esim-for-china-travel/) — buy now, activate when visa is approved.
2. **Alipay:** [Setup guide →](/posts/alipay-foreigner-setup-guide/) — link your bank card.
3. **Cash backup:** Carry some RMB or USD as emergency backup.

📌 **Source:** [NIA China](https://www.nia.gov.cn/) · Last verified: **2026-06-04**

⚠️ This is not legal advice. Visa policies change. Always confirm with your local Chinese embassy before booking.
"""


def slug(name):
    return name.lower().replace(" ", "-").replace("'", "")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Track already-existing manually written files to skip them
    existing = set(os.listdir(OUTPUT_DIR)) - {"_index.md"}

    generated = 0
    for c in COUNTRIES:
        filename = slug(c["name"]) + ".md"
        if filename in existing:
            continue

        status = c["status"]
        notes = c.get("notes", "")

        if status == "visa-free":
            content = TEMPLATE.format(
                name=c["name"], flag=c["flag"], region=c["region"],
                policy=c["policy"], status=status,
                notes=f"**Key fact:** {notes}" if notes else ""
            )
        elif status == "transit":
            content = TRANSIT_TEMPLATE.format(
                name=c["name"], flag=c["flag"], region=c["region"],
                policy=c["policy"], status=status,
                notes=f"**Note:** {notes}" if notes else ""
            )
        else:
            content = VISA_REQUIRED_TEMPLATE.format(
                name=c["name"], flag=c["flag"], region=c["region"],
                policy=c["policy"], status=status,
                notes=f"**Current situation:** {notes}" if notes else ""
            )

        filepath = os.path.join(OUTPUT_DIR, filename)
        with open(filepath, "w") as f:
            f.write(content)
        generated += 1

    print(f"Generated {generated} new country pages.")


if __name__ == "__main__":
    main()
