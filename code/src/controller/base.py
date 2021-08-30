from src.libs import response
from typing import Dict
from src import app


class BaseController:
    def __init__(self, name: str, repository):
        self.name = name
        self.repository = repository
        self.response = response

    def insert(self, **payload: Dict) -> Dict:
        data = self.repository.insert(**payload)
        if data:
            return self.response.successWithData(data=data.to_dict(), message=f"{self.name} created succesfully", statusCode=201), 201

    def get_by_id(self, id: str) -> Dict:
        data = self.repository.get_by_id(id)
        if data:
            return self.response.successWithData(data=data.to_dict(), message=f"{self.name} fetched succesfully", statusCode=201)
        return self.response.error(message="No record found", statusCode=404), 404

    def get_docs(self, **query: Dict) -> Dict:
        data = self.repository.get_docs(**query)
        return self.response.successWithData(data=[item.to_dict() for item in data] or [], message=f"{self.name} fetched succesfully", statusCode=200)

    def update(self, id, **payload):
        data = self.repository.update(id=id, **payload)
        if data:
            return self.response.successWithData(data=data.to_dict(), message=f"{self.name} updated successfully", statusCode=200)
        return self.response.error(message="No record found", statusCode=404), 404

    def delete(self, id):
        data = self.repository.delete(id=id)
        if data:
            return self.response.successWithData(data=data.to_dict(), message=f"{self.name} deleted successfully", statusCode=200)
        return self.response.error(message="No record found", statusCode=404), 404
