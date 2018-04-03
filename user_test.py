import unittest
import pyperclip
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

    def tearDown(self):
        """
        tearDown method that does cleanup after each test case has run
        """
        User.user_list = []

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

    def test_save_multiple_user(self):
        """
        test_save_multiple_user to check if we can save multiple user objects to our user_list
        """
        self.new_user.save_user()
        test_user = User("site","fname","h8wh83h")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        """
        test_delete_user to test if we can remove a user from our user_list
        """
        self.new_user.save_user()
        test_user = User("site", "fname", "h8wh83h")
        test_user.save_user()
        self.new_user.delete_user()#Deleting a user
        self.assertEqual(len(User.user_list),1)

    def test_find_user_by_user_name(self):
        """
        test to check if we can find a user by username and display information
        """
        self.new_user.save_user()
        test_user = User("site", "fname", "h8wh83h")
        test_user.save_user()
        found_user = User.find_by_user_name("fname")
        self.assertEqual(found_user.password,test_user.password)

    def test_user_exists(self):
        """
        test to check if we can return a boolean if we cannot find the user.
        """
        self.new_user.save_user()
        test_user = User("site", "fname", "h8wh83h")
        test_user.save_user()
        user_exists = User.user_exist("fname")
        self.assertTrue(user_exists)

    def test_display_all_users(self):
        """
        method that returns a list of all saved user_list
        """
        self.assertEqual(User.display_users(),User.user_list)

    def test_copy_password(self):
        """
        Test to confirm that we are copying the password from an existing user
        """
        self.new_user.save_user()
        User.copy_password("remmy")
        self.assertEqual(self.new_user.password,pyperclip.paste())


if __name__ == '__main__':
    unittest.main()
