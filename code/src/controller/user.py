from src.controller.base import BaseController
from src.repositories.user import UserRepository
from src import app


class UserController(BaseController):
    def __init__(self):
        self.name = 'User'
        self.repository = UserRepository()
        super().__init__(name=self.name, repository=self.repository)

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

    def login(self, **payload):
        try:
            username = payload.get('username')
            password = payload.get('password')
            user = self.repository.get_docs(raw=True, username=username)
            if user is None:
                raise Exception("Incorrect Email or Password")
            else:
                is_correct = user[0].check_password_correction(password)
                if is_correct:
                    auth_token = user[0].encode_auth_token(
                        user[0].to_dict().get('_id', None))
                    response_data = {
                        **user[0].to_dict(), 'auth_token': auth_token.decode('utf-8')}
                    return self.response.successWithData(data=response_data, message=f"{self.name} logged in successfully", statusCode=200), 200
                return self.response.error(message="Incorrect Credentials, Please try again"), 400

        except Exception as error:
            app.logger.error(error)
            return self.response.error(message=str(error), statusCode=400), 400
