import unittest

from flask import url_for
from flask_testing import TestCase
from application.app import birthDate

from app import app

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
        self.assertEqual(birthDate(1986),'432', msg='Equal')
        self.assertEqual(birthDate(2002),'240', msg='Equal')
        self.assertEqual(birthDate('abc'), 'ValueError: enter a number', msg='Equal')
