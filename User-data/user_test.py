import unittest
from user import User

class TestContact(unittest.TestCase):
    """
    Test class that defines test cases for the user class behaviour.

    Args:
    unittest.TestCase: TestCase class that helps in creating test cases.
    """
    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_user = User("Facebook", "remmy", "34y8")

    def test_init(self):
