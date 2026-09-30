# Garden App (Task 48)

This project is a small gardening advice app that gives tips based on month and season.

## Files

- `garden_advice.py` - refactored app logic with functions and a small CLI.
- `test_garden_advice.py` - unit tests for month parsing, season mapping, and validation.
- `repo.txt` - place your public GitHub repository URL here.

## Run locally

```powershell
python garden_advice.py
```

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
Month: March
Hemisphere (north/south, default north): south

Season: Summer
```
