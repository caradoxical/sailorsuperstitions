"""Main superstition checking functionality."""

import json
import os
from typing import Dict, Optional


class SuperstitionChecker:
    """Check sailing conditions against maritime superstitions."""

    def __init__(self):
        """Initialize the checker with superstition data."""
        self.superstitions = self._load_superstitions()
        self.active_curses = []

    def _load_superstitions(self) -> Dict:
        """Load superstitions from JSON file."""
        data_path = os.path.join(
            os.path.dirname(__file__), "data", "superstitions.json"
        )
        with open(data_path, "r") as f:
            return json.load(f)

    def check_condition(self, condition_id: str) -> Optional[Dict]:
        """Check if a specific condition triggers a superstition.

        Args:
            condition_id: The ID of the condition to check

        Returns:
            Superstition details if found, None otherwise
        """
        for superstition in self.superstitions["superstitions"]:
            if superstition["id"] == condition_id:
                self.active_curses.append(superstition)
                return superstition
        return None

    def calculate_curse_level(self) -> int:
        """Calculate total curse level from all active superstitions.

        Returns:
            Total curse level (can be negative for good luck!)
        """
        return sum(curse["severity"] for curse in self.active_curses)

    def get_fortune(self) -> str:
        """Get overall fortune based on curse level.

        Returns:
            Fortune message based on current curse level
        """
        level = self.calculate_curse_level()

        if level >= 15:
            return "☠️  DOOMED! Consider a career on land."
        elif level >= 10:
            return "⚠️  Severe curse detected. Postpone voyage!"
        elif level >= 5:
            return "⛵ Choppy waters ahead. Proceed with caution."
        elif level > 0:
            return "🌊 Minor bad luck. Keep your wits about you."
        elif level == 0:
            return "⚓ Neutral fortune. The sea is indifferent."
        else:
            return "🌟 Blessed voyage! The sea gods smile upon you!"

    def clear_curses(self):
        """Clear all active curses."""
        self.active_curses = []
