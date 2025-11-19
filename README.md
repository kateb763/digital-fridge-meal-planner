# Digital Fridge — Meal Planner

A small desktop/mobile app to track fridge contents and suggest meals.

## Overview

Digital Fridge is a lightweight meal-planning app built with Python and Kivy. It helps you
manage items in your fridge, classify food images, import product data from OpenFoodFacts,
and generate simple meal suggestions based on available ingredients.

## Key Features

- Track fridge items and quantities (`fridge.py`, `food_item.py`).
- Classify food images locally (`image_classifier.py`).
- Import product data from OpenFoodFacts (`openfoodfacts_loader.py`).
- Suggest meals from available ingredients (`meal_planner.py`).
- Simple Kivy-based GUI (`main.py`, `main.kv`).

## Requirements

- macOS (development). The app is cross-platform but was developed with macOS in mind.
- Python 3.8+ (use a virtual environment).
- System dependencies for Kivy if running on desktop (see Kivy docs).
- Project Python dependencies listed in `requirements.txt`.

## Quick Start (macOS / local desktop)

1. Create and activate a virtual environment (zsh):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install Python dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

3. Run the app:

```bash
python main.py
```

The Kivy GUI should open. Use the UI to add food items, scan images, or generate meal suggestions.

## Running the image classifier or loaders

- To run the image classifier from the command line (if provided):

```bash
python image_classifier.py --help
```

- To load data from OpenFoodFacts programmatically or via script:

```bash
python openfoodfacts_loader.py --help
```

Check the top of each script for usage examples and available command-line flags.

## Notes about iOS / Mobile

This repository contains a `kivy-ios/` folder and related toolchain files. Building for iOS
requires the `kivy-ios` toolchain and an Xcode/macOS build environment. Typical steps are:

1. Follow `kivy-ios` docs to install the toolchain and create a project.
2. Use `toolchain build` to compile Python libraries for iOS.
3. Open the generated Xcode project and build to a device or simulator.

Refer to the `kivy-ios` documentation for up-to-date build instructions.

## Project Structure (top-level files)

- `main.py` — Kivy app entry point.
- `main.kv` — Kivy layout definitions and UI rules.
- `fridge.py` — Fridge management logic and persistence.
- `food_item.py` — Food item model and helpers.
- `image_classifier.py` — Image classification utilities.
- `meal_planner.py` — Meal suggestion logic.
- `openfoodfacts_loader.py` — Helpers to fetch/parse OpenFoodFacts data.
- `user_info.py` — User preferences and profile management.
- `requirements.txt` — Python package requirements.
- `kivy-ios/` — Toolchain and packaging files for building iOS apps.

## How It Works (high-level)

- The app maintains an in-memory (and/or on-disk) list of `FoodItem` objects managed by
  `Fridge` (see `food_item.py` & `fridge.py`).
- The classifier (`image_classifier.py`) can be used to guess an item's identity from a photo.
- Product metadata can be found and imported using `openfoodfacts_loader.py` to enrich items.
- `meal_planner.py` contains simple heuristics to propose recipes or meal ideas based on
  ingredients currently in the fridge.

## Development

- Please run the app in a virtual environment to avoid package conflicts.
- Follow PEP 8 and project code style when contributing.

Suggested editor/IDE commands (zsh):

```bash
# format with black (if used)
black .

# run a linter (if you use flake8)
flake8 .
```

## Contributing

Contributions are welcome. Typical contribution flow:

1. Fork the repo and create a feature branch.
2. Run and test your changes locally.
3. Open a pull request describing the changes and reasoning.

If you plan on significant changes (refactorings, storage updates, replacing the classifier),
open an issue first to discuss the design.

## Troubleshooting

- If Kivy fails to start, ensure system dependencies (SDL, GStreamer, etc.) are installed
  per the official Kivy documentation.
- If you receive import errors, confirm you're using the correct Python interpreter and the
  virtual environment is activated.

## License

No license was detected in this repository root. Add a `LICENSE` file to declare the project's
license (for example, `MIT`, `Apache-2.0`, etc.).

## Next Steps / Ideas

- Add persistent storage (SQLite) for fridge state and user settings.
- Add unit tests for `meal_planner.py` and `fridge.py`.
- Improve classifier accuracy or integrate an external model service.

---

If you'd like, I can also:

- add a short `CONTRIBUTING.md`,
- detect and add a recommended `LICENSE` file,
- or create a small sample dataset and tests for the meal planner.

File created: `README.md`

