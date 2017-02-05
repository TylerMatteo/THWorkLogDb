from peewee import *
import datetime

db = SqliteDatabase('worklog.db')


class Entry(Model):
    created_by = CharField(max_length=255)
    created_at = DateTimeField(default=datetime.datetime.now())
    name = CharField(max_length=255)
    minutes = IntegerField()

    class Meta:
        database = db

    def __str__(self):
        notesConcatenated = "".join(str(note) + '\n' for note in self.notes)
        return """{}: {} - {}\nTime Spent: {}\nNotes:\n{}
                """.format(self.created_by, self.name, self.created_at,
                           self.minutes, notesConcatenated)
