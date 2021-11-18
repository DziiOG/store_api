
from marshmallow import Schema, fields, validate, validates
from src.helpers.misc import ROLES, Status
from marshmallow_enum import EnumField


class UserSignUpValidation(Schema):
    email = fields.Email(required=True, validate=validate.Email(error="Please provide valid email"))
    roles = EnumField(ROLES, required=True, error="Role is not accepted")
    status = EnumField(Status, error="Invalid status")
    username = fields.String(required=True, validate=validate.Length(min=4, error="Username should not be less than 4 characters"))
    password = fields.String(required=True, validate=validate.Length(min=8, error="Password should not be less than 8 characters"))
    confirm_password = fields.String(required=True)
    avatar = fields.String(required=False)
    

    

class UserLoginValidation(Schema):
    email = fields.Email(required=True, validate=validate.Email(error="Please provide valid email"))
    password = fields.String(required=True)

class UserQueryValidation(Schema):
    username = fields.String(required=False)
