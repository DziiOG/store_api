
from flask import jsonify


class BaseController:
    def __init__(self, name, repository, response):
        self.name = name
        self.repository = repository
        self.response = response
    

    def insert(self, **payload):
        try: 
            data = self.repository.insert(**payload)
            if data:
                return self.response.successWithData(data=data, message=f"{self.name} created succesfully", statusCode=201), 201 
        except Exception as error:
            return self.response.error(message=str(error), statusCode=400), 400

    def get_by_id(self, id):
        try:
            data = self.repository.get_by_id(id)
            if data:
                return self.response.successWithData(data=data, message=f"{self.name} fetched succesfully", statusCode=201)
            return self.response.error(message="No record found", statusCode=404), 404
        except Exception as error:
            return self.response.error(message=str(error), statusCode=400), 400

    def get_docs(self, **query):
        try:
            data = self.repository.get_docs(**query)
            if data:
                return self.response.successWithData(data=data, message=f"{self.name} fetched succesfully", statusCode=200)
            return self.response.error(message="No record found", statusCode=404), 404
        except Exception as error:
            return self.response.error(message=str(error), statusCode=400), 400
            

    def update(self, id, payload):
        try:
            data = self.repository.update(id=id, payload=payload)
            if data:
                return self.response.successWithData(data=data, message=f"{self.name} updated successfully", statusCode=200)
            return self.response.error(message="Error occurred", statusCode=404), 404
        except Exception as error:
            return self.response.error(message=str(error), statusCode=400), 400


    def delete(self, id):
        try:
            data = self.repository.delete(id=id)
            if data:
                return self.response.successWithData(data=data, message=f"{self.name} deleted successfully", statusCode=200)
            return self.response.error(message="Error occured while deleting", statusCode=404)
        except Exception as error:
            return self.response.error(message=str(error), statusCode=400), 400



    