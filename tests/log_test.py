import unittest
from unittest import mock
from log import Log
from peewee import *
import pdb

class LogTest(unittest.TestCase):

	def setUp(self):
		db = SqliteDatabase('worklog.db')
		self.log = Log()

	def test_lookup_by_date(self):
		#log = Log()
		self.log.print_all_by_date = mock.Mock(return_value=None)
		self.log.lookup('d')
		assert self.log.print_all_by_date.called

	def test_lookup_by_employee(self):
		#log = Log()
		self.log.find_by_employee = mock.Mock(return_value=None)
		with unittest.mock.patch('builtins.input', return_value='John'):
			self.log.lookup('e')
			assert self.log.find_by_employee.called

	def test_lookup_by_search(self):
		#log = Log()
		self.log.find_by_search = mock.Mock(return_value=None)
		with unittest.mock.patch('builtins.input', return_value='Test'):
			self.log.lookup('s')
			assert self.log.find_by_search.called




