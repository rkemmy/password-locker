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
