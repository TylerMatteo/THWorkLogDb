from note import Note


class Entry:

    def __init__(self, name, minutes, timestamp, notes):
        self.name = name
        self.minutes = minutes
        self.timestamp = timestamp
        self.notes = []
        for note in notes:
            self.add_note(note)

    def __str__(self):
        notesConcatenated = "".join(str(note) + '\n' for note in self.notes)
        return """{} - {}\nTime Spent: {}\nNotes:\n{}
                """.format(self.name, self.timestamp,
                           self.minutes, notesConcatenated)

    def add_note(self, noteText):
        self.notes.append(Note(noteText))
