
class BaseRepository:
    def __init__(self, model):
        self.model = model
    
    def insert(self, **payload):
        try:
            data = self.model(**payload).save()
            if data:
                return data.to_dict()
        except Exception as error:
            raise error
            

    def get_by_id(self, id):
        try:
            data = self.model.objects().get(id=id)
            if data:
                return data.to_dict()
        except Exception as error:
            raise error

    def get_docs(self, **query):
        try:
            data = self.model.objects().filter(**query)
            if data:
                return [item.to_dict() for item in data]
        except Exception as error:
            raise error

            
    def update(self, id, **payload):
        try:
            data =  self.model.objects(id=id).update(**payload)
            if data:
                updated_data = self.model.objects().get(id=id)
                if updated_data:
                    return updated_data.to_dict()
        except Exception as error:
            raise error

    def delete(self, id):
        try:            
            data = self.model.objects.get(id=id)
            data.delete()
            if data:
                return data.to_dict()
        except Exception as error:
            print(error)
            raise error

    


