import unittest

from garden_advice import advice_for, get_season, normalize_month


class GardenAdviceTests(unittest.TestCase):
    def test_normalize_month_name(self):
        self.assertEqual(normalize_month("March"), 3)

    def test_normalize_month_number_string(self):
        self.assertEqual(normalize_month("11"), 11)

    def test_normalize_month_rejects_invalid_values(self):
        for month in (0, 13, "Marh", ""):
            with self.subTest(month=month):
                with self.assertRaises(ValueError):
                    normalize_month(month)

    def test_season_by_hemisphere(self):
        self.assertEqual(get_season("January", "north"), "summer")
        self.assertEqual(get_season("January", "south"), "spring")

    def test_every_month_maps_to_season_in_both_hemispheres(self):
        northern_seasons = (
            "summer", "summer", "autumn", "autumn", "autumn", "winter",
            "winter", "winter", "spring", "spring", "spring", "summer",
        )
        southern_seasons = (
            "spring", "spring", "summer", "summer", "summer", "autumn",
            "autumn", "autumn", "winter", "winter", "winter", "spring",
        )

        for month, season in enumerate(northern_seasons, start=1):
            with self.subTest(month=month, hemisphere="north"):
                self.assertEqual(get_season(month, "north"), season)

        for month, season in enumerate(southern_seasons, start=1):
            with self.subTest(month=month, hemisphere="south"):
                self.assertEqual(get_season(month, "south"), season)

    def test_month_and_hemisphere_ignore_case_and_whitespace(self):
        self.assertEqual(normalize_month(" MARCH "), 3)
        self.assertEqual(get_season(" MARCH ", "South"), "summer")

    def test_advice_contains_season_and_tips(self):
        advice = advice_for("September", "north")
        self.assertIn("Season: Spring", advice)
        self.assertIn(
            "Start new seedlings and feed plants as growth accelerates.",
            advice,
        )
        self.assertIn(
            "Plant herbs and quick crops for a productive season start.",
            advice,
        )

    def test_invalid_hemisphere(self):
        with self.assertRaises(ValueError):
            get_season("June", "east")


if __name__ == "__main__":
    unittest.main()
