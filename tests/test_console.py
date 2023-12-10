#!/usr/bin/python3
"""
Contains the class TestConsoleDocs
"""

import console
import inspect
import pep8
import unittest
from unittest.mock import patch
from io import StringIO
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

HBNBCommand = console.HBNBCommand


class TestConsoleDocs(unittest.TestCase):
    """Class for testing documentation of the console"""

    def test_pep8_conformance_console(self):
        """Test that console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(["console.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_pep8_conformance_test_console(self):
        """Test that tests/test_console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(["tests/test_console.py"])
        self.assertEqual(
            result.total_errors, 0, "Found code style errors (and warnings)."
        )

    def test_console_module_docstring(self):
        """Test for the console.py module docstring"""
        self.assertIsNot(console.__doc__, None, "console.py needs a docstring")
        self.assertTrue(
            len(console.__doc__) >= 1, "console.py needs a docstring"
        )

    def test_HBNBCommand_class_docstring(self):
        """Test for the HBNBCommand class docstring"""
        self.assertIsNot(
            HBNBCommand.__doc__, None, "HBNBCommand class needs a docstring"
        )
        self.assertTrue(
            len(HBNBCommand.__doc__) >= 1,
            "HBNBCommand class needs a docstring"
        )


class TestConsoleCommands(unittest.TestCase):
    """Class for testing documentation of the console help command"""

    def test_help_command(self):
        """Test the help command"""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("help")
            output = mock_stdout.getvalue().strip()
            self.assertIn("Documented commands", output)

    def test_show_command(self):
        """Test the show command"""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("help show")
            output = mock_stdout.getvalue().strip()
            self.assertIn("Show instance that been passed", output)

    def test_create_command(self):
        """Test the create command"""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("help create")
            output = mock_stdout.getvalue().strip()
            self.assertIn("Creates an instance", output)

    def test_update_command(self):
        """Test the update command"""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("help update")
            output = mock_stdout.getvalue().strip()
            self.assertIn(
                "Updates instances based on the class name and id", output)

    def test_destroy_command(self):
        """Test the destroy command"""
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("help destroy")
            output = mock_stdout.getvalue().strip()
            self.assertIn("Destorys an instance that been passed", output)


class TestConsoleEOFCommand(unittest.TestCase):
    """Class for testing documentation of the console EOF command"""

    def test_eof_command(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("EOF")
            output = mock_stdout.getvalue().strip()
            self.assertIn("", output)


class TestConsoleAllCommand(unittest.TestCase):
    """Class for testing documentation of the console EOF command"""

    def test_all_command_base_model(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            _ = BaseModel()
            console.HBNBCommand().onecmd("all")
            output = mock_stdout.getvalue().strip()
            self.assertIn("BaseModel", output)

    def test_all_command_amenity(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            _ = Amenity()
            console.HBNBCommand().onecmd("all")
            output = mock_stdout.getvalue().strip()
            self.assertIn("Amenity", output)

    def test_all_command_city(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            _ = City()
            console.HBNBCommand().onecmd("all")
            output = mock_stdout.getvalue().strip()
            self.assertIn("City", output)

    def test_all_command_place(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            _ = Place()
            console.HBNBCommand().onecmd("all")
            output = mock_stdout.getvalue().strip()
            self.assertIn("Place", output)

    def test_all_command_review(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            _ = Review()
            console.HBNBCommand().onecmd("all")
            output = mock_stdout.getvalue().strip()
            self.assertIn("Review", output)

    def test_all_command_state(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            _ = State()
            console.HBNBCommand().onecmd("all")
            output = mock_stdout.getvalue().strip()
            self.assertIn("State", output)

    def test_all_command_user(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            _ = User()
            console.HBNBCommand().onecmd("all")
            output = mock_stdout.getvalue().strip()
            self.assertIn("User", output)

    def test_all_command_base_model_argument(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("all BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertIn("[BaseModel]", output)

    def test_all_command_amenity_argument(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("all Amenity")
            output = mock_stdout.getvalue().strip()
            self.assertIn("[Amenity]", output)

    def test_all_command_city_argument(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("all City")
            output = mock_stdout.getvalue().strip()
            self.assertIn("[City]", output)

    def test_all_command_place_argument(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("all Place")
            output = mock_stdout.getvalue().strip()
            self.assertIn("[Place]", output)

    def test_all_command_review_argument(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("all Review")
            output = mock_stdout.getvalue().strip()
            self.assertIn("[Review]", output)

    def test_all_command_state_argument(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("all State")
            output = mock_stdout.getvalue().strip()
            self.assertIn("[State]", output)

    def test_all_command_user_argument(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("all User")
            output = mock_stdout.getvalue().strip()
            self.assertIn("[User]", output)

    def test_all_command_invalid_argument(self):
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            console.HBNBCommand().onecmd("all Base")
            output = mock_stdout.getvalue().strip()
            self.assertIn("**", output)


if __name__ == '__main__':
    unittest.main()
