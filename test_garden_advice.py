import unittest
from unittest.mock import DEFAULT, patch

from garden_advice import advice_for, get_season, main, normalize_month


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


class GardenAdviceGuiTests(unittest.TestCase):
    def setUp(self):
        widgets = patch.multiple(
            "garden_advice.tk", Tk=DEFAULT, Label=DEFAULT,
            Entry=DEFAULT, Button=DEFAULT,
        )
        self.widgets = widgets.start()
        self.addCleanup(widgets.stop)
        combobox = patch("garden_advice.ttk.Combobox")
        self.combobox = combobox.start()
        self.addCleanup(combobox.stop)
        showerror = patch("garden_advice.messagebox.showerror")
        self.showerror = showerror.start()
        self.addCleanup(showerror.stop)

        main()
        self.root = self.widgets["Tk"].return_value
        self.month_entry = self.widgets["Entry"].return_value
        self.result_label = self.widgets["Label"].return_value
        self.submit = self.widgets["Button"].call_args.kwargs["command"]

    def test_gui_displays_advice_via_button_and_enter(self):
        self.root.title.assert_called_once_with("Garden Advice App")
        self.combobox.assert_called_once_with(
            self.root, values=["north", "south"], state="readonly", width=22
        )
        self.combobox.return_value.set.assert_called_once_with("north")
        self.root.bind.assert_called_once_with("<Return>", self.submit)
        self.root.mainloop.assert_called_once_with()

        for month, hemisphere in [("March", "north"), ("6", "south")]:
            with self.subTest(month=month, hemisphere=hemisphere):
                self.month_entry.get.return_value = month
                self.combobox.return_value.get.return_value = hemisphere
                self.submit(None)
                self.result_label.config.assert_called_with(
                    text=advice_for(month, hemisphere)
                )
        self.showerror.assert_not_called()

    def test_invalid_input_shows_popup_and_allows_retry(self):
        self.combobox.return_value.get.return_value = "north"
        for month in ["", "invalid", "0", "13"]:
            with self.subTest(month=month):
                self.month_entry.get.return_value = month
                self.month_entry.focus_set.reset_mock()
                self.submit()
                with self.assertRaises(ValueError) as error:
                    advice_for(month, "north")
                self.showerror.assert_called_with("Input error", str(error.exception))
                self.month_entry.focus_set.assert_called_once_with()
                self.month_entry.select_range.assert_called_with(0, "end")
                self.result_label.config.assert_not_called()
                self.root.destroy.assert_not_called()
                self.root.quit.assert_not_called()

        self.month_entry.get.return_value = "January"
        self.submit()
        self.result_label.config.assert_called_once_with(
            text=advice_for("January", "north")
        )
        self.assertEqual(self.showerror.call_count, 4)


if __name__ == "__main__":
    unittest.main()
