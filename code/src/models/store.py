

from src.models.item import ItemModel
from src.config.db import db
from flask import jsonify
from bson import ObjectId
import datetime


class StoreModel(db.Document):
    name = db.StringField(required=True, unique=True)
    items = db.ListField(db.LazyReferenceField('ItemModel'))
    creation_date = db.DateTimeField()
    modified_date = db.DateTimeField(default=datetime.datetime.now)

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.datetime.now()
        self.modified_date = datetime.datetime.now()
        return super(StoreModel, self).save(*args, **kwargs)

    def update(self, *args, **kwargs):
        self.modified_date = datetime.datetime.now()
        return super(StoreModel, self).update(*args, **kwargs)

    def to_dict(self):
        return{
            '_id':  str(self.pk),
            'name': self.name,
            'items': [ ItemModel.objects().get(id=item.pk).to_dict() for item in self.items if item],
            'createdAt': self.creation_date.strftime("%m/%d/%Y, %H:%M:%S"),
            'updatedAt': self.modified_date.strftime("%m/%d/%Y, %H:%M:%S")
        }
