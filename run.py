#!/usr/bin/env python3.6
from usercredentials import users, Credentials

def create_user(firstname,secondname,username,password):
    '''
    Function to create a new user
    '''
    new_user = users(firstname,secondname,username,password)
    return new_user
def store_user(user):
    '''
    Function to store user information
    '''
    users.store_user(user)
def  user_exists(username,password):
    '''
    Function that checks if user exits
    '''
    return Credentials.user_exists(username,password)
def create_credential(username,password,account_name):
    '''
    Function that creates credential
    '''

    return Credentials(username,password,account_name)
def  save_credential(credential):
    '''
    Function that saves new credential
    '''
    credential.save_credential()
def generate_password(Credentials):
    '''
    Function that generates random password
    '''
    return Credentials.generate_password()
def display_credentials():
    '''
    Function that displays credential
    '''
    return Credentials.display_credentials()
def find_by_account(name):
    '''
    Function that finds credential by account name
    '''
    return Credentials.find_by_account(name)

