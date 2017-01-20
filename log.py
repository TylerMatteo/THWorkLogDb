from entry import Entry
from note import Note
import re
import datetime

class Log:

    # Creates a new entry in this log
    def new(self):
        username = input("What is your name? ")
        task_name = input("What would you like to name this task? ")
        while True:
            try:
                minutes = input("How many minutes have you "
                                "spent working on it? ")
                new_entry = Entry.create(created_by=username,
                                         name=task_name, minutes=minutes)
                break
            except ValueError:
                print("Invalid input. Please enter a number of minutes.")
        while True:
            noteText = input('Please enter notes for this task. '
                             'Enter "q" to finish. ')
            if noteText.upper() == "Q":
                break
            else:
                Note.create(entry=new_entry, content=noteText, 
                            created_at=datetime.datetime.now())

    # Wrapper function to prompt user for lookup type
    def lookup(self):
        while True:
            option = input("Would you like to lookup by [d]ate, "
                           "[e]mployee, or [s]earch term? ")

            if option.upper() == "D":
                self.find_by_date(datetime.datetime.now())
                break
            elif option.upper() == "E":
                phrase = input("What employee name would you like to search for? ")
                self.find_by_employee(phrase)
                break
            # elif option.upper() == "P":
            #     pattern = input("What regex would you like to search for? ")
            #     self.find_by_pattern(pattern)
            #     break
            else:
                print("Invalid option, please try again.")

    def find_by_date(self, date):
        # User set() to generate a unique,
        # sorted list of dates that have entries
        uniqueDates = list(set([entry.timestamp.date() for entry
                                in self.entries]))
        sortedDates = sorted(uniqueDates)

        # Print the list of dates and prompt for a selection
        for i, date in enumerate(sortedDates):
            print("{}: {}".format(i+1, date.strftime('%b %d, %Y')))

        while True:
            try:
                dateSelection = int(input("Select a date to "
                                          "view by number. "))
                if dateSelection in list(range(1, len(sortedDates)+1)):
                    break
                else:
                    print("That number isn't in the list of options. "
                          "Please try again.")
                    continue
            except ValueError:
                print('Not a valid input, please try again.')
                continue

        # Print all entries for the chosen date
        print("".join([str(entry) + '\n' for entry in self.entries
                      if entry.timestamp.date()
                      == sortedDates[dateSelection - 1]]))

    def find_by_employee(self, name):
        # Use a comprehension to grab all notes with the
        # given number of minutes
        matches = Entry.get(Entry.created_by == name)

        print("".join([str(entry) + '\n' for entry in matches]))

    # def find_by_exact_match(self, phrase):
    #     # Use a comprehension to grab all entries containing the
    #     # given phrase in their title or note
    #     matches = [entry for entry in self.entries if phrase in entry.name
    #                or any([note.content for note in entry.notes])]

    #     print("".join([str(entry) + '\n' for entry in matches]))

    # def find_by_pattern(self, pattern):
    #     # Use a comprehension to grab all entries that have a title or
    #     # note content matching the given pattern
    #     matches = [entry for entry in self.entries
    #                if re.search(pattern, entry.name) is not None
    #                or any([re.search(pattern, note.content)
    #                        for note in entry.notes])]

        print("".join([str(entry) + '\n' for entry in matches]))
