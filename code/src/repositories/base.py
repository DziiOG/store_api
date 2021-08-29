from typing import List, Dict
from src.validations.item import ItemBodyValidation
import json

class BaseRepository:
    def __init__(self, model):
        self.model = model

    def insert(self, **payload: Dict) -> Dict:
            data = self.model(**payload).save()
            if data:
                return data.to_dict()
        

    def get_by_id(self, id: str) -> Dict:
            data = self.model.objects().get(id=id)
            if data:                
                return data.to_dict()
        

    def get_docs(self, raw=False, **query) -> List[Dict]:
            data = self.model.objects().filter(**query)
            if data and raw is False:
                return [item.to_dict() for item in data]
            else:
                if data and raw is True:
                    return [item for item in data]
        

    def update(self, id, **payload) -> Dict:
            data = self.model.objects(id=id).update(**payload)
            if data:
                updated_data = self.model.objects().get(id=id)
                if updated_data:
                    return updated_data.to_dict()
        

    def delete(self, id) -> Dict:
            data = self.model.objects.get(id=id)
            data.delete()
            if data:
                return data.to_dict()
        
