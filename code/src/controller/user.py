from src.controller.base import BaseController
from src import app


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
            app.logger.error(error)
            return self.response.error(message=str(error), statusCode=400), 400

        # # if user exists raise error
        # except Exception as error:
        #     self.response.error(message=str(error))

    def login(self, **payload):
        try:
            username = payload.get('username')
            password = payload.get('password')
            user = self.repository.get_docs(username=username)
            if user:
                is_correct = user.check_password_correction(password)

                if is_correct:
                    auth_token = user.encode_auth_token(
                        user.to_dict().get('_id', None))

                    response_data = {
                        **user.to_dict(), 'auth_token': auth_token}

                    return self.response.successWithData(data=response_data, message=f"{self.name} logged in successfully", statusCode=201)

            else:
                raise Exception("Incorrect Email or Password")

        except Exception as error:
            app.logger.error(error)
            return self.response.error(message=str(error), statusCode=400), 400
