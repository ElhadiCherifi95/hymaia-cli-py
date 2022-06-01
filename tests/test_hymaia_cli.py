import unittest
from unittest.mock import MagicMock
from hymaia_cli.command.command import *


class TestCommand(unittest.TestCase):
    def test_get_base_url(self):
        # GIVEN
        # WHEN
        actual_base_url = Command.get_base_url(config_path="tests/resources/config.ini")

        # THEN
        expected_base_url = "https://test.execute-api.eu-west-3.amazonaws.com/hymaia-cli"
        self.assertEqual(expected_base_url, actual_base_url)

    def test_get_url_with_parameter(self):
        # GIVEN
        Command.get_base_url = MagicMock(return_value="https://test.execute-api.eu-west-3.amazonaws.com/hymaia-cli")
        command = Command(name="test", url_parameter="test/command-test")

        # WHEN
        actual_base_url, actual_base_parameter = command.get_url_with_parameter()

        # THEN
        expected_base_url, expected_base_parameter = "https://test.execute-api.eu-west-3.amazonaws.com/hymaia-cli", \
                                                     "test/command-test"
        self.assertEqual(expected_base_url, actual_base_url)
        self.assertEqual(expected_base_parameter, actual_base_parameter)
