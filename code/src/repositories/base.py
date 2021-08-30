from typing import List, Dict
from mongoengine import DoesNotExist
from src.validations.item import ItemBodyValidation
import json


class BaseRepository:
    def __init__(self, model):
        self.model = model

    def insert(self, **payload: Dict):
      try:  
        data = self.model(**payload).save()
        return data
      except DoesNotExist:
          return None
          

    def get_by_id(self, id: str):
        try:
            data = self.model.objects().get(id=id)
            return data
        except DoesNotExist:
            return None

    def get_docs(self, **query):
       try:
            data = self.model.objects().filter(**query)
            return [item for item in data]
           
       except DoesNotExist:
           return []

    def update(self, id, **payload):
        try:
            data = self.model.objects(id=id).update(**payload)
            if data:
                updated_data = self.model.objects().get(id=id)
                if updated_data:
                    return updated_data
        except DoesNotExist:
            return None

    def delete(self, id):
        try:
            data = self.model.objects.get(id=id)
            data.delete()
            if data:
                return data
        except DoesNotExist:
            return None
