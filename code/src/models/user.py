from src.config.db import db
from marshmallow import ValidationError
from src import bcrypt
import datetime


class UserModel(db.Document):
    username = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    creation_date = db.DateTimeField()
    modified_date = db.DateTimeField(default=datetime.datetime.now)

    def clean(self):
        if self.password is not None:
            if len(self.password) < 6:
                raise ValidationError("Too short password.")
        self.password = bcrypt.generate_password_hash(
            self.password).decode('utf-8')

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.datetime.now()
        self.modified_date = datetime.datetime.now()
        return super(UserModel, self).save(*args, **kwargs)

    def update(self, *args, **kwargs):
        self.modified_date = datetime.datetime.now()
        return super(UserModel, self).update(*args, **kwargs)
    
    def to_dict(self):
        return dict(
            _id=str(self.pk),
            username=self.username,
            createdAt=self.creation_date.strftime("%m/%d/%Y, %H:%M:%S"),
            updatedAt=self.modified_date.strftime("%m/%d/%Y, %H:%M:%S")
        )
