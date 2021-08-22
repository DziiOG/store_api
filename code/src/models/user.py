from src.config.db import db
import datetime


class UserModel(db.Document):
    username = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    creation_date = db.DateTimeField()
    modified_date = db.DateTimeField(default=datetime.datetime.now)


    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.datetime.now()
        self.modified_date = datetime.datetime.now()
        return super(UserModel, self).save(*args, **kwargs)

    def update(self, *args, **kwargs):
        self.modified_date = datetime.datetime.now()
        return super(UserModel, self).update(*args, **kwargs)



