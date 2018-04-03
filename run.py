#!/usr/bin/env python3.6
from user import User

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

def main():
    print("Hello welcome to password locker. What is your username?")
    username = input()

    print(f"Hi {username}. What would you like to find?")
    print('\n')

    while True:
        print()
