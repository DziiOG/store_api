from src.libs import response
from pyee import EventEmitter
from typing import Dict


class BaseController(EventEmitter):
    def __init__(self, name: str, repository, listening: bool = False):
        self.repository = repository
        self.listening = listening
        self.response = response
        self.name = name
        super().__init__()

    def insert(self, **payload: Dict) -> Dict:
        data = self.repository.insert(**payload)
        self.listening and self.emit('insert', data)
        return self.response.successWithData(data=data.to_dict() if data else None, message=f"{self.name} created successfully", statusCode=201), 201

    def get_by_id(self, id: str) -> Dict:
        data = self.repository.get_by_id(id)
        if data:
            return self.response.successWithData(data=data.to_dict(), message=f"{self.name} fetched successfully", statusCode=201)
        return self.response.error(message="No record found", statusCode=404), 404

    def get_docs(self, **query: Dict) -> Dict:
        data = self.repository.get_docs(**query)
        return self.response.successWithData(data=[item.to_dict() for item in data] or [], message=f"{self.name} fetched successfully", statusCode=200)

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
