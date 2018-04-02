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
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_user.site_name,"Facebook")
        self.assertEqual(self.new_user.user_name,"remmy")
        self.assertEqual(self.new_user.password,"34y8")

    def test_save_user(self):
        """test_save_user test case to test if the user object is saved into the user user_list
        """
        self.new_user.save_user() #saving the new users
        self.assertEqual(len(User.user_list), 1)


if __name__ == '__main__':
    unittest.main()
