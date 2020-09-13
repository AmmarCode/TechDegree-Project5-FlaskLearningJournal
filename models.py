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

    @classmethod
    def create_post(cls, post_id, title, date, time_spent, what_you_learned, resources):
        try:
            cls.create(
                post_id=post_id,
                title=title,
                date=date,
                time_spent=time_spent,
                learned=learned,
                resources=resources
            )
        except IntegrityError:
            raise ValueError("Post already exists")


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Post], safe=True)
    DATABASE.close()    
