# ⚓ Sailor's Superstitions

A fun and whimsical Python package that checks sailing conditions against maritime superstitions and provides mystical predictions for your voyage!

## Overview

Sailor's Superstitions is a lightweight Python package designed to help sailors and nautical enthusiasts check their sailing conditions against classic maritime superstitions. It calculates a "curse level" based on various superstitious conditions and provides fortunes and sailing wisdom to guide your journey.

## Features

- **SuperstitionChecker**: Check your sailing conditions against a comprehensive database of maritime superstitions
- **Curse Level Calculation**: Get a combined curse level based on all active superstitions
- **Fortune Telling**: Receive personalized fortunes based on your curse level
- **Sailing Wisdom**: Get random pieces of classic sailing advice and maritime wisdom
- **Interactive Demo**: Run an interactive script to check multiple conditions and get your sailing fortune

## Installation

Install from Anaconda.org:

```bash
conda install -c caradoxical sailorsuperstitions
```

Or install from source:

```bash
git clone https://github.com/caradoxical/sailorsuperstitions.git
cd sailorsuperstitions
pip install -e .
```

## Usage

### Basic Example

```python
from sailorsuperstitions import SuperstitionChecker
from sailorsuperstitions.fortune import FortuneTeller

# Create a superstition checker
checker = SuperstitionChecker()

# Check specific sailing conditions
checker.check_condition("friday_departure")  # Sailing on Friday?
checker.check_condition("bananas")           # Bananas on board?
checker.check_condition("whistling")         # Someone whistling on deck?

# Calculate your curse level
curse_level = checker.calculate_curse_level()
print(f"Curse Level: {curse_level}")

# Get a fortune based on your curse level
print(checker.get_fortune())

# Get a personalized daily fortune
fortune_teller = FortuneTeller()
print(fortune_teller.get_daily_fortune(curse_level))

# Get random sailing wisdom
print(fortune_teller.get_random_advice())
```

### Interactive Demo

Run the included demo script for an interactive experience:

```bash
python demo.py
```

This will guide you through checking various sailing conditions and calculate your overall fortune.

## Superstitions Included

The package checks for conditions such as:
- Departing on a Friday
- Bananas on board (bad luck!)
- Whistling on deck
- Renaming the boat
- Black cats aboard
- Women on board (historically considered bad luck in maritime tradition)
- And more!

## API Reference

### SuperstitionChecker

```python
checker = SuperstitionChecker()
```

**Methods:**

- `check_condition(condition_id: str) -> Optional[Dict]`: Check if a specific condition triggers a superstition
- `calculate_curse_level() -> int`: Get the total curse level from all active superstitions
- `get_fortune() -> str`: Get a fortune message based on the current curse level
- `clear_curses()`: Reset all active superstitions

### FortuneTeller

```python
teller = FortuneTeller()
```

**Methods:**

- `get_daily_fortune(curse_level: int) -> str`: Get a personalized fortune based on curse level
- `get_random_advice() -> str`: Get a random piece of sailing wisdom

## Requirements

- Python 3.8 or higher

## License

MIT License - See LICENSE file for details

## Author

Seth Clark (caradoxical@gmail.com)

## Disclaimer

This package is for entertainment purposes only. While maritime superstitions have a rich history, actual sailing safety should always be determined by weather conditions, proper equipment, and sound nautical practices. May the wind be at your back! 🌊⛵
