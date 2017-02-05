from entry import Entry
from note import Note
import datetime


class Log:

    # Takes in details and creates a new entry in this log.
    def add_entry(self, username, task_name, minutes):
        minutes = int(minutes)
        new_entry = Entry.create(created_by=username,
                                 name=task_name, minutes=minutes)
        while True:
            noteText = input('Please enter notes for this task. '
                             'Enter "q" to finish. ')
            if noteText.upper() == "Q":
                break
            else:
                Note.create(entry=new_entry, content=noteText,
                            created_at=datetime.datetime.now())

    # Wrapper function to prompt user for lookup type
    def lookup(self, option):
        if option.upper() == "D":
            self.print_all_by_date()
        elif option.upper() == "E":
            phrase = input("What employee name would you like to search for? ")
            self.find_by_employee(phrase)
        elif option.upper() == "S":
            pattern = input("What term would you like to search for? ")
            self.find_by_search(pattern)

    def print_all_by_date(self):
        entries = Entry.select().order_by(Entry.created_at)
        date = entries[0].created_at.date()
        print(date)
        for entry in entries:
            if entry.created_at.date() != date:
                date = entry.created_at
                print(date)
            print(entry)

    def find_by_employee(self, name):
        return Entry.select().where(Entry.created_by == name)

    def find_by_search(self, phrase):
        return Entry.select().join(Note).where(
                (Entry.name.contains(phrase)) |
                (Note.content.contains(phrase)))

    def print_entries(self, entries):
        for entry in entries:
            print(entry)
