import unittest
from usercredentials import users, Credentials

class TestUser(unittest.TestCase):
    def setUp(self):
        '''
        Create user before every test
        '''
        self.new_user = users('Florence','Nyaoke','flonyaks','p@ssw0rd1')

    def test__init__(self):
        '''
        test that initialization was done well
        '''
        self.assertEqual(self.new_user.firstname,'Florence')
        self.assertEqual(self.new_user.secondname,'Nyaoke')
        self.assertEqual(self.new_user.password,'p@ssw0rd1')
        self.assertEqual(self.new_user.username,'flonyaks')

    def test_store_user(self):
        self.new_user.store_user()
        self.assertEqual(len(users.list_user),1)

    def tearDown(self):
        '''
        to undo the tests before this
        '''
        users.list_user=[]
