from entry import Entry
from peewee import *

db = SqliteDatabase('worklog.db')


class Note(Model):
    entry = ForeignKeyField(Entry, related_name='notes')
    content = CharField(max_length=255)
    created_at = DateTimeField()

    class Meta:
        database = db

    def __str__(self):
        template = '%b %d, %Y - %H:%M:%S'
        return "{}\n-{}".format(self.content,
                                self.created_at.strftime(template))
