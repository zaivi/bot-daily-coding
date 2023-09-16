#!/usr/bin/env python

"""Tests for `bot_daily_coding` package."""


import unittest
from click.testing import CliRunner

from bot_daily_coding import bot_daily_coding
from bot_daily_coding import cli


class TestBot_daily_coding(unittest.TestCase):
    """Tests for `bot_daily_coding` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'bot_daily_coding.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
