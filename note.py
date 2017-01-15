import datetime


class Note:

    def __init__(self, content):
        self.content = content
        self.createdAt = datetime.datetime.now()

    def __str__(self):
        template = '%b %d, %Y - %H:%M:%S'
        return "{}\n-{}".format(self.content,
                                self.createdAt.strftime(template))
