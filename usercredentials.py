import pyperclip
import random
import string
global list_user

class users:
    '''
    class to create users and save their information
    '''

    list_user = []
    def __init__(self, firstname, secondname,username,password):
        '''
         method to initialize properties that each  user object will hold
        '''
        self.firstname = firstname
        self.secondname = secondname
        self.username = username
        self.password = password
    def store_user(self):
        '''
        method to save user
        '''
        users.list_user.append(self)
class Credentials:
    
    account_credentials = []

    
    
    def __init__(self,username,password,account_name):
        '''
         method to initialize properties that each  credentials object will hold
        '''
        self.username = username
        self.password = password
        self.account_name = account_name

