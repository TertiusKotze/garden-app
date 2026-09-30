"""Garden advice app with month and season based tips.

This module provides small, testable functions so the logic is easy to
maintain and extend.
"""

from __future__ import annotations

MONTH_TO_NUMBER = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
}

SEASON_BY_MONTH = {
    "north": {
        "summer": {12, 1, 2},
        "autumn": {3, 4, 5},
        "winter": {6, 7, 8},
        "spring": {9, 10, 11},
    },
    "south": {
        "spring": {12, 1, 2},
        "summer": {3, 4, 5},
        "autumn": {6, 7, 8},
        "winter": {9, 10, 11},
    },
}

SEASON_TIPS = {
    "summer": "Water early in the morning and mulch to reduce evaporation.",
    "autumn": "Add compost and clean up fallen leaves to prevent disease.",
    "winter": "Protect sensitive plants from frost and reduce watering frequency.",
    "spring": "Start new seedlings and feed plants as growth accelerates.",
}

MONTH_TIPS = {
    1: "Plan your planting calendar and check seed stock.",
    2: "Prune fruit trees and prepare beds for upcoming planting.",
    3: "Sow leafy greens and monitor for early pests.",
    4: "Harden off seedlings before transplanting outdoors.",
    5: "Stake climbing plants and maintain consistent watering.",
    6: "Top-dress soil with compost to maintain nutrients.",
    7: "Inspect for pests weekly and remove affected leaves quickly.",
    8: "Deadhead flowering plants to promote continuous blooms.",
    9: "Plant herbs and quick crops for a productive season start.",
    10: "Divide overcrowded perennials and refresh mulching.",
    11: "Check irrigation systems and prepare shade cloth if needed.",
    12: "Review this year\'s garden notes and plan improvements.",
}


def normalize_month(month: str | int) -> int:
    """Return a month number from either month name or month index."""
    if isinstance(month, int):
        if 1 <= month <= 12:
            return month
        raise ValueError("Month number must be between 1 and 12.")

    value = str(month).strip().lower()
    if value.isdigit():
        month_number = int(value)
        if 1 <= month_number <= 12:
            return month_number
        raise ValueError("Month number must be between 1 and 12.")

    if value in MONTH_TO_NUMBER:
        return MONTH_TO_NUMBER[value]

    raise ValueError("Month must be a full name (e.g. March) or number (1-12).")


def get_season(month: str | int, hemisphere: str = "north") -> str:
    """Determine season for a month in either northern or southern hemisphere."""
    month_number = normalize_month(month)
    hemisphere_key = hemisphere.strip().lower()
    if hemisphere_key not in SEASON_BY_MONTH:
        raise ValueError("Hemisphere must be 'north' or 'south'.")

    for season, months in SEASON_BY_MONTH[hemisphere_key].items():
        if month_number in months:
            return season

    raise RuntimeError("Unexpected season mapping issue.")


def advice_for(month: str | int, hemisphere: str = "north") -> str:
    """Build gardening advice for the provided month and hemisphere."""
    month_number = normalize_month(month)
    season = get_season(month_number, hemisphere)
    season_tip = SEASON_TIPS[season]
    month_tip = MONTH_TIPS[month_number]
    return f"Season: {season.title()}\n- {season_tip}\n- {month_tip}"


def main() -> None:
    """Simple CLI entrypoint."""
    print("Garden Advice App")
    print("Enter month as full name (e.g. March) or number (1-12).")
    while True:
        raw_month = input("Month: ").strip()
        raw_hemisphere = input("Hemisphere (north/south, default north): ").strip() or "north"

        try:
            print("\n" + advice_for(raw_month, raw_hemisphere))
            break
        except ValueError as error:
            print(f"Input error: {error}\nPlease try again.\n")


if __name__ == "__main__":
    main()

