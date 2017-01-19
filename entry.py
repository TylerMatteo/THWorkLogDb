

from peewee import *

db = SqliteDatabase('worklog.db')


class Entry(Model):
    created_by = CharField(max_length=255)
    name = CharField(max_length=255)
    minutes = IntegerField()

    class Meta:
        database = db

    def __str__(self):
        notesConcatenated = "".join(str(note) + '\n' for note in self.notes)
        return """{} - {}\nTime Spent: {}\nNotes:\n{}
                """.format(self.name, self.timestamp,
                           self.minutes, notesConcatenated)

    def add_note(self, noteText):
        self.notes.append(Note(noteText))

