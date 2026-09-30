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

    def test_advice_contains_season(self):
        advice = advice_for("September", "north")
        self.assertIn("Season: Spring", advice)

    def test_invalid_hemisphere(self):
        with self.assertRaises(ValueError):
            get_season("June", "east")


if __name__ == "__main__":
    unittest.main()

