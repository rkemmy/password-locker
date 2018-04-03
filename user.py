import pyperclip

class User:
    """
    Class that generates new instances of users
    """

    user_list = [] #Empty user list

    def __init__(self, site_name, user_name, password):
        """
        __init__ method that helps us define properties for our objects.

        Args:
            user_name: New user user_name.
            password : New password.

        """
        self.site_name = site_name
        self.user_name = user_name
        self.password = password

    def save_user(self):
        """
        save_user method saves user objects into user_list
        """
        User.user_list.append(self)

    def delete_user(self):
        """
        delete_usermethod deletes a saved user from the user list
        """
        User.user_list.remove(self)
    @classmethod
    def find_by_user_name(cls,user_name):
        """
        Method that takes in a username and returns a user that matches that username.

        Args:
            user_name: Username to search for
        Returns :
            details of user that matches the username.
        """
        for user in cls.user_list:
            if user.user_name == user_name:
                return user

    @classmethod
    def user_exist(cls,user_name):
        """
        Method that checks if a user exists from the user list.

        Args:
            user_name: Username to search for
        Returns :
            Boolean: True or false depending if the user exists
        """
        for user in cls.user_list:
            if user.user_name == user_name:
                return True
        return False

    @classmethod
    def display_users(cls):
        """
        method that returns the user user list
        """
        return cls.user_list

    @classmethod
    def copy_password(cls,user_name):
        user_found = User.find_by_user_name(user_name)
        pyperclip.copy(user_found.password)
