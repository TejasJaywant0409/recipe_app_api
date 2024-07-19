from django.test import SimpleTestCase
from unittest.mock import patch
from django.core.management import call_command
from psycopg2 import OperationalError as psycopg2OpError
from django.db.utils import OperationalError


@patch('core.management.commands.wait_for_db.Command.check')
class CommandsTests(SimpleTestCase):

    def test_wait_for_db_ready(self, patched_check):
        patched_check.return_value = True
        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        patched_check.side_effect = [psycopg2OpError] * 2 + \
            [OperationalError] * 3 + [True]
        call_command('wait_for_db')

        # Check if the patched_check was called 6 times
        self.assertEqual(patched_check.call_count, 6)
