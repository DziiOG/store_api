from src.controller.base import BaseController


class UserController(BaseController):
    def __init__(self, name, repository, response):
        super().__init__(name, repository, response)

    def sign_up(self, **payload):
        try:
            # check if user already exists by using username
            username = payload.get('username')
            data = self.repository.get_docs(username=username)
            if data is not None:
                raise Exception("User already exists")
            else:
                data = {
                    'username': username,
                    'password': payload.get('password')
                }
                result = self.repository.insert(**data)
                if result:
                    return self.response.successWithData(data=result, message=f"{self.name} created succesfully", statusCode=201), 201
        except Exception as error:
            return self.response.error(message=str(error), statusCode=400), 400

        # if user exists raise error
        except Exception as error:
            self.response.error(message=str(error))
