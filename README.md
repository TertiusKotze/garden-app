# Garden App (Task 48)

This project is a small gardening advice app that gives tips based on month and season.

## Files

- `garden_advice.py` - refactored app logic with functions and a small Tkinter GUI.
- `test_garden_advice.py` - unit tests for month parsing, season mapping, validation, and GUI interactions.
- `repo.txt` - place your public GitHub repository URL here.

## Run locally

```powershell
python garden_advice.py
```

Requires Python with Tkinter and a graphical desktop. If Tkinter is missing on
Debian/Ubuntu, install it with `sudo apt install python3-tk`.

Enter a full month name or a number from 1 to 12, select a hemisphere (defaults
to north), then click **Get advice** or press **Enter**. Advice appears in the
window. Invalid input shows an error pop-up; dismiss it and correct the selected
month text to try again without restarting the app.

## Run tests

```powershell
python -m unittest -v
```

## Suggested issues for your GitHub workflow

Create these two issues in your GitHub repo:

1. Refactor `garden_advice.py` into reusable functions
2. Add tests and improve documentation

## Suggested branch names

- `feature/refactor-garden-advice`
- `feature/tests-and-docs`

## Suggested commit messages

- `Refactor garden advice logic into reusable functions (closes #1)`
- `Add unit tests and README usage instructions (closes #2)`

## Suggested PR titles

- `Refactor garden advice script into testable functions`
- `Add tests and documentation for garden advice app`

After each merge, update your local main branch:

```powershell
git checkout main
git pull origin main
```


## Example

```text
Season: Summer
- Water early in the morning and mulch to reduce evaporation.
- Sow leafy greens and monitor for early pests.
```

Shown in the window for March with the south hemisphere selected.
