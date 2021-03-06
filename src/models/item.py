

from src.config.db import db
import datetime


class ItemModel(db.Document):
    name = db.StringField(required=True, unique=True)
    price = db.FloatField(required=True)
    creation_date = db.DateTimeField()
    modified_date = db.DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.datetime.now()
        self.modified_date = datetime.datetime.now()
        return super(ItemModel, self).save(*args, **kwargs)

    def update(self, *args, **kwargs):
        self.modified_date = datetime.datetime.now()
        return super(UserModel, self).update(*args, **kwargs)

    def to_dict(self):
        return{
            '_id':  str(self.pk),
            'name': self.name,
            'price': self.price,
            'createdAt': self.creation_date.strftime("%m/%d/%Y, %H:%M:%S"),
            'updatedAt': self.modified_date.strftime("%m/%d/%Y, %H:%M:%S")
        }
