import random

class Credentials:
    """
    Class that generates new instance of credentials
    """
    credentials_list = []
    def __init__(self,password):
        """__init__ method that helps define the properties for our object credentials_list
        """
        self.password = password


    @classmethod
    def generate_password(cls, password_length):
        chars ="abcdefghijklmnopqrstuvwxyz1234567890"
        password_generate = "".join(random.sample(chars,int(password_length)))
        password = password_generate
        return password
