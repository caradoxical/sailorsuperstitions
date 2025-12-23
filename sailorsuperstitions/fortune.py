"""Fortune telling and advice module."""

import random


class FortuneTeller:
    """Provide sailing advice and mystical predictions."""

    def __init__(self):
        """Initialize with sailing wisdom."""
        self.sailing_advice = {
            "storm": [
                "Red sky at night, sailor's delight. Red sky at morning, sailors take warning.",
                "When the wind is from the East, 'tis neither good for man nor beast.",
                "Mackerel sky and mare's tails make tall ships carry low sails.",
            ],
            "luck": [
                "A sailor's best friend is a well-tied knot and a short memory.",
                "The cure for anything is salt water: sweat, tears, or the sea.",
                "Fair winds and following seas await those who respect the ocean.",
            ],
            "blessing": [
                "May your anchor be tight, your cork be loose, your rum be spiced, and your compass be true.",
                "May the wind always be at your back and the sun upon your face.",
                "Smooth seas never made a skilled sailor.",
            ],
        }

    def get_daily_fortune(self, curse_level: int) -> str:
        """Generate personalized fortune based on curse level.

        Args:
            curse_level: Current curse level from SuperstitionChecker

        Returns:
            Personalized sailing fortune
        """
        if curse_level >= 10:
            return self._get_doom_fortune()
        elif curse_level >= 5:
            return self._get_warning_fortune()
        elif curse_level > 0:
            return self._get_caution_fortune()
        else:
            return self._get_blessing_fortune()

    def _get_doom_fortune(self) -> str:
        """Return fortune for doomed voyages."""
        dooms = [
            "The Kraken stirs in its slumber. Perhaps tomorrow is better for sailing.",
            "Even Davy Jones thinks you should reconsider.",
            "The stars spell 'N-O-P-E' in maritime semaphore.",
        ]
        return random.choice(dooms)

    def _get_warning_fortune(self) -> str:
        """Return fortune for risky voyages."""
        warnings = [
            "The sea is angry. Bring extra life jackets.",
            "Neptune is in a mood. Proceed with offerings of rum.",
            "Your nautical karma needs adjustment. Consider charitable donations to sea turtles.",
        ]
        return random.choice(warnings)

    def _get_caution_fortune(self) -> str:
        """Return fortune for slightly unlucky voyages."""
        cautions = [
            "Minor squalls in your future. Nothing a seasoned sailor can't handle.",
            "The dolphins are gossiping about you. It's mostly neutral.",
            "Your sea legs are 73% ready. Close enough!",
        ]
        return random.choice(cautions)

    def _get_blessing_fortune(self) -> str:
        """Return fortune for blessed voyages."""
        blessings = [
            "Mermaids sing your praises! (The good kind, not the sirens)",
            "Favorable winds and Instagram-worthy sunsets ahead!",
            "The sea whispers your name with affection. Sail forth!",
        ]
        return random.choice(blessings)

    def get_random_advice(self) -> str:
        """Get random sailing wisdom.

        Returns:
            Random piece of sailing advice
        """
        category = random.choice(list(self.sailing_advice.keys()))
        return random.choice(self.sailing_advice[category])
