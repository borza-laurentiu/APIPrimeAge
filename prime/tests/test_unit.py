import unittest

from flask import url_for
from flask_testing import TestCase

from app import app
from application import prime

class TestBase(TestCase):
    def create_app(self):
        config_name = 'testing'
        app.config.update(
            WTF_CSRF_ENABLED = False,
            DEBUG = True
        )
        return app

    def setUp(self):
        print("-----------")


    def tearDown(self):
         print("-----------")

class TestPrime(unittest.TestCase):

    def test_values(self):

        self.assertEqual(prime(1986), 'No, you are COMPOSITE', msg='Equal')
        self.assertEqual(prime(1987), 'Yes, you are PRIME', msg='Equal')
        self.assertEqual(prime(2), 'Yes, you are PRIME', msg='Equal')
        self.assertEqual(prime(1), 'You do not appear to exist', msg='Equal')
        self.assertEqual(prime(0), 'You do not appear to exist', msg='Equal')
        self.assertEqual(prime(-1986), 'You do not appear to exist', msg='Equal')




