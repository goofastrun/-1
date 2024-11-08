import unittest
from unittest.mock import patch
from emulator import ShellEmulator
from datetime import datetime

class TestShellEmulator(unittest.TestCase):
    def setUp(self):
        self.emulator = ShellEmulator("config.toml")
        self.emulator.mkdir('some_directory')

    def test_cd(self):
        self.emulator.cd('some_directory')
        self.assertEqual(self.emulator.current_dir, 'some_directory')

    def test_invalid_cd(self):
        with self.assertRaises(ValueError):
            self.emulator.cd('invalid_directory')

    def test_ls(self):
        self.emulator.mkdir('test_dir')
        self.assertIn('test_dir', self.emulator.ls())

    def test_mkdir(self):
        self.emulator.mkdir('new_dir')
        self.assertIn('new_dir', self.emulator.ls())

    def test_cal(self, mock_print):
        self.emulator.cal()
        current_date = datetime.now().strftime("%B %Y")
        mock_print.assert_called_once_with(current_date)

if __name__ == '__main__':
    unittest.main()
