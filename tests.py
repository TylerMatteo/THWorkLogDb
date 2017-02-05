import unittest
from unittest import mock
from log import Log
from entry import Entry
from note import Note
import datetime
from peewee import *
import pdb

class LogTest(unittest.TestCase):
    #     self.entries = [
    #     Entry(
    #         'test1',
    #         datetime.timedelta(minutes=10),
    #         datetime.datetime(year=2016, day=11, month=12),
    #         ['test1 note']
    #     ),
    #     Entry(
    #         'test2',
    #         datetime.timedelta(minutes=20),
    #         datetime.datetime(year=2016, day=11, month=12),
    #         ['test2 note']
    #     ),
    #     Entry(
    #         'test3',
    #         datetime.timedelta(minutes=30),
    #         datetime.datetime(year=2016, day=12, month=12),
    #         ['test3 note']
    #     )
    # ]
    
    def setUp(self):
        self.db = SqliteDatabase(':memory:')
        self.db.connect()
        self.db.create_tables([Entry, Note], safe=True)
        self.log = Log()
        self.test_entry1 = Entry.create(created_by="tester1",
                           name="Entry 1", minutes=10,
                           created_at=datetime.datetime(day=1,month=1,year=2016))
        self.test_entry2 = Entry.create(created_by="tester2",
                           name="Entry 2", minutes=20,
                           created_at=datetime.datetime(day=1,month=2,year=2016))
        self.test_entry3 = Entry.create(created_by="tester3",
                           name="Entry 3", minutes=30,
                           created_at=datetime.datetime(day=1,month=3,year=2016))
        self.test_note = Note.create(entry=self.test_entry3, content="Test note", 
                            created_at=datetime.datetime.now())

    def test_add_entry(self):
        with unittest.mock.patch('builtins.input', side_effect = ["Note1", 
                                                                  "Note2", 
                                                                  "q"]):
            self.log.add_entry("tester", "Test add entry", 40)
            test_entry = Entry.get(Entry.name == "Test add entry")
            self.assertEqual(test_entry.minutes, 40)
            self.assertEqual(test_entry.notes[0].content,"Note1")

    def test_lookup_by_date(self):
        self.log.print_all_by_date = mock.Mock(return_value=None)
        self.log.lookup('d')
        assert self.log.print_all_by_date.called

    def test_lookup_by_employee(self):
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

    def test_find_by_employee(self):
        entries = self.log.find_by_employee("tester1")
        self.assertEqual(entries[0].name, self.test_entry1.name)

    def test_find_by_search_in_name(self):
        entries = self.log.find_by_search("Entry 3")
        self.assertEqual(entries[0].name, self.test_entry3.name)

    def test_find_by_search_in_note(self):
        entries = self.log.find_by_search("Test note")
        self.assertEqual(entries[0].name, self.test_entry3.name)


class EntryTest(unittest.TestCase):

    def setUp(self):
        pass
        # self.db = SqliteDatabase(':memory:')
        # self.db.connect()
        # self.db.create_tables([Entry, Note], safe=True)

    def test_str(self):
        test_entry = Entry.create(created_by="tester1",
                           name="Entry 1", minutes=10,)
        entry_string = str(test_entry)
        for val in "tester1", "Entry 1", "10":
            self.assertIn(val, entry_string)

if __name__ == "__main__":
    unittest.main()