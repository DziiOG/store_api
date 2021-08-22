
from marshmallow import Schema, fields, validate


class UserSignUpValidation(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)
    confirm_password = fields.String(required=True)

class UserLoginValidation(Schema):
    username = fields.String(required=True)
    password = fields.String(required=True)

class UserQueryValidation(Schema):
    username = fields.String()
