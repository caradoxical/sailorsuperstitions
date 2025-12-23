#!/usr/bin/env python
"""Demo script for the sailorsuperstitions package."""

from sailorsuperstitions import SuperstitionChecker
from sailorsuperstitions.fortune import FortuneTeller


def main():
    """Run an interactive sailing superstition check."""
    print("⚓ Welcome to the Maritime Superstition Checker ⚓")
    print("=" * 50)

    checker = SuperstitionChecker()
    fortune_teller = FortuneTeller()

    # Interactive check
    print("\nLet's check your sailing conditions...")
    print("\nAvailable conditions to check:")
    print("- bananas (Do you have bananas on board?)")
    print("- whistle (Did someone whistle on deck?)")
    print("- friday_departure (Are you leaving on a Friday?)")
    print("- rename_boat (Did you rename the vessel?)")
    print("- black_cat (Is there a black cat aboard?)")
    print("- womens_presence (Are there women on board?)")
    print()

    while True:
        condition = input(
            "Enter a condition to check (or 'done' to calculate): "
        ).strip()

        if condition.lower() == "done":
            break

        result = checker.check_condition(condition)
        if result:
            print(f"✓ {result['message']}")
        else:
            print("❌ Unknown condition. Try again!")

    # Calculate final fortune
    print("\n" + "=" * 50)
    curse_level = checker.calculate_curse_level()
    print(f"\n🎲 Total Curse Level: {curse_level}")
    print(f"\n🔮 Fortune: {checker.get_fortune()}")
    print(f"\n💭 {fortune_teller.get_daily_fortune(curse_level)}")
    print(f"\n⛵ Sailing Wisdom: {fortune_teller.get_random_advice()}")
    print("\n" + "=" * 50)

    if curse_level >= 10:
        print("\n🚨 RECOMMENDATION: Maybe stay in port today...")
    else:
        print("\n✨ Fair winds and following seas!")


if __name__ == "__main__":
    main()
