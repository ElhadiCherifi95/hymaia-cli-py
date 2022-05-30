import unittest

from hymaia_cli.command.command import *


class TestCommand(unittest.TestCase):
    def test_get_url_with_parameter(self):
        # GIVEN
        input_str = "Bonjour bonjour, je m'appelle Franck"
        expected = [('Bonjour', 1), ('bonjour,', 1), ('je', 1), ("m'appelle", 1), ('Franck', 1)]

        # WHEN
        actual = wordcount(input_str)

        # THEN
        self.assertEqual(expected, actual)
