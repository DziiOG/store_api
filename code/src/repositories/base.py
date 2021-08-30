from typing import List, Dict
from src.validations.item import ItemBodyValidation
import json


class BaseRepository:
    def __init__(self, model):
        self.model = model

    def insert(self, **payload: Dict):
        data = self.model(**payload).save()
        if data:
            return data

    def get_by_id(self, id: str):
        data = self.model.objects().get(id=id)
        if data:
            return data

    def get_docs(self, **query):
        data = self.model.objects().filter(**query)
        if data:
            return [item for item in data]

    def update(self, id, **payload):
        data = self.model.objects(id=id).update(**payload)
        if data:
            updated_data = self.model.objects().get(id=id)
            if updated_data:
                return updated_data

    def delete(self, id):
        data = self.model.objects.get(id=id)
        data.delete()
        if data:
            return data
