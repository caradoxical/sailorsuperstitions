"""Tests for the SuperstitionChecker."""

from sailorsuperstitions import SuperstitionChecker


class TestSuperstitionChecker:
    """Test the main superstition checking functionality."""

    def setup_method(self):
        """Set up test fixtures."""
        self.checker = SuperstitionChecker()

    def test_initialization(self):
        """Test checker initializes correctly."""
        assert self.checker is not None
        assert len(self.checker.superstitions["superstitions"]) > 0
        assert self.checker.active_curses == []

    def test_check_condition_valid(self):
        """Test checking a valid condition."""
        result = self.checker.check_condition("bananas")
        assert result is not None
        assert result["id"] == "bananas"
        assert result["severity"] == 10

    def test_check_condition_invalid(self):
        """Test checking an invalid condition."""
        result = self.checker.check_condition("flying_dutchman")
        assert result is None

    def test_calculate_curse_level_empty(self):
        """Test curse level with no active curses."""
        assert self.checker.calculate_curse_level() == 0

    def test_calculate_curse_level_single(self):
        """Test curse level with one curse."""
        self.checker.check_condition("whistle")
        assert self.checker.calculate_curse_level() == 7

    def test_calculate_curse_level_multiple(self):
        """Test curse level with multiple curses."""
        self.checker.check_condition("bananas")
        self.checker.check_condition("friday_departure")
        assert self.checker.calculate_curse_level() == 16

    def test_calculate_curse_level_mixed(self):
        """Test curse level with good and bad luck."""
        self.checker.check_condition("bananas")  # +10
        self.checker.check_condition("black_cat")  # -3
        assert self.checker.calculate_curse_level() == 7

    def test_get_fortune_doomed(self):
        """Test fortune for doomed voyage."""
        self.checker.check_condition("bananas")
        self.checker.check_condition("whistle")
        fortune = self.checker.get_fortune()
        assert "DOOMED" in fortune

    def test_clear_curses(self):
        """Test clearing all curses."""
        self.checker.check_condition("bananas")
        self.checker.check_condition("whistle")
        assert len(self.checker.active_curses) == 2

        self.checker.clear_curses()
        assert len(self.checker.active_curses) == 0
        assert self.checker.calculate_curse_level() == 0
