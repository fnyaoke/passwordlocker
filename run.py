#!/usr/bin/env python3.6
from usercredentials import users, Credentials

def create_user(firstname,secondname,username,password):
    '''
    Function to create a new user
    '''
    new_user = users(firstname,secondname,username,password)
    return new_user