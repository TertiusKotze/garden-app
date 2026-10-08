import unittest

from garden_advice import advice_for, get_season, normalize_month


class GardenAdviceTests(unittest.TestCase):
    def test_normalize_month_name(self):
        self.assertEqual(normalize_month("March"), 3)

    def test_normalize_month_number_string(self):
        self.assertEqual(normalize_month("11"), 11)

    def test_season_by_hemisphere(self):
        self.assertEqual(get_season("January", "north"), "summer")
        self.assertEqual(get_season("January", "south"), "spring")

    def test_season_lookup_for_every_month(self):
        north = (
            "summer", "summer", "autumn", "autumn", "autumn", "winter",
            "winter", "winter", "spring", "spring", "spring", "summer",
        )
        south = (
            "spring", "spring", "summer", "summer", "summer", "autumn",
            "autumn", "autumn", "winter", "winter", "winter", "spring",
        )
        for month, expected in enumerate(north, start=1):
            self.assertEqual(get_season(month, "north"), expected)
        for month, expected in enumerate(south, start=1):
            self.assertEqual(get_season(month, "south"), expected)

    def test_advice_contains_season(self):
        advice = advice_for("September", "north")
        self.assertIn("Season: Spring", advice)

    def test_invalid_hemisphere(self):
        with self.assertRaisesRegex(
            ValueError, "^Hemisphere must be 'north' or 'south'\\.$"
        ):
            get_season("June", "east")

    def test_invalid_month_error_message(self):
        with self.assertRaisesRegex(
            ValueError, "^Month number must be between 1 and 12\\.$"
        ):
            get_season(13)
        with self.assertRaisesRegex(
            ValueError,
            "^Month must be a full name \\(e.g. March\\) or number \\(1-12\\)\\.$",
        ):
            get_season("not a month")


if __name__ == "__main__":
    unittest.main()
