#!/usr/bin/env python3.6
from user import User
from credentials import Credentials

def create_user(sitename,username,passlock):
    """
    Function to create a new user
    """
    new_user = User(sitename,username,passlock)
    return new_user

def save_users(user):
    """
    Function to save users
    """
    user.save_user()

def del_user(user):
    """
    Function to delete a user
    """
    user.delete_user()

def find_user(user_name):
    """
    Function to check if a user exists by user name and returns that user
    """
    return User.find_by_user_name(user_name)

def check_existing_users(user_name):
    """
    Function that checks if a user exists with that username and returns a Boolean
    """
    return User.user_exist(user_name)

def display_users():
    """
    Function that returns all the saved users
    """
    return User.display_users()

def generate_password(password_length):
    return Credentials.generate_password(password_length)

def main():
    print("Hello welcome to password locker. What is your username?")
    username = input()

    print(f"Hi {username}. What would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : uc-create a new user, du - display users, fu- find a user, gp-generate password, ex- exit the user list")
        short_code = input().lower()
        if short_code == 'uc':
            print("New User")
            print("-"*10)

            print(" Choose a Site")
            sitename = input()

            print("Enter your Username")
            username = input()

            print("Create a Password")
            passlock = input()

            save_users(create_user(sitename,username,passlock))#create and save new contact
            print('\n')
            print(f"New User {sitename} {username} {passlock} created")
            print('\n')

        elif short_code == 'du':
            if display_users():
                print("Here is a list of all your passwords")
                print('\n')
                for user in display_users():
                    print(f"New User {sitename} {username} {passlock}")
                    print('\n')
                else:
                    print('\n')
                    print("You don't seem to have any passwords saved yet")
                    print('\n')

        elif short_code == 'fu':
            print("Enter the username you want to search for")
            search_user = input()
            if check_existing_users(search_user):
                search_user = find_user(search_user)
                print(f"{search_user.site_name}")
                print('-' * 20)
                print(f"Username....{search_user.user_name}")
                print(f"Password....{search_user.password}")
            else:
                print("That user does not exist")

        elif short_code == 'gp':
            print('')
            print('How long would you like your password to be?')
            password_length = int(input())
            password = generate_password(password_length)
            print(f"Your password is : {password}")

        elif short_code == 'ex':
            print("Exiting")
            break
    else:
        print("That short_code is invalid")

if __name__ == '__main__':
    main()
