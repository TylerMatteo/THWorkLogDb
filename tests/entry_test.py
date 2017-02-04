import unittest
from entry import Entry
from peewee import *

class EntryTest(unittest.TestCase):

	def setUp(self):
		db = SqliteDatabase('worklog.db')

	# def test_one_plus_two(self):
	# 	assert 1 + 2 == 2
