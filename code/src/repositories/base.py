
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
            data = self.model.objects.first_or_404(_id=id)
            if data:
                return data
        except Exception as error:
            raise error

    def get_docs(self, **query):
        try:
            data = self.model.objects(**query).filter()
            if data:
                return [item.to_dict() for item in data]
        except Exception as error:
            raise error


            
    def update(self, id, **payload):
        try:
            data =  self.model.objects(_id=id).update(**payload)
            if data:
                return data
        except Exception as error:
            raise error

    def delete(self, id):
        try:            
            data = self.model.objects.get(_id=id)
            data.delete()
            if data:
                return data
        except Exception as error:
            print(error)
            raise error

    


