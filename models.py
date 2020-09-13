from datetime import datetime
from peewee import *


DATABASE = SqliteDatabase("journals.db")

class Post(Model):
    post_id = IntegerField(primary_key=True)
    title = CharField(max_length=200)
    date = DateField(default=datetime.utcnow)
    time_spent = IntegerField()
    learned = TextField()
    resources = TextField()

    class Meta:
        database = DATABASE
        order_by = ("-date",)


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Post], safe=True)
    DATABASE.close()    
