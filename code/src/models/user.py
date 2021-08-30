from werkzeug.security import safe_str_cmp
from src.helpers.misc import Status, ROLES
from datetime import datetime, timedelta
from flask import url_for, request
from requests import Response
from src.config.config import CONFIG
from src.config.db import db
from src.libs.mailgun import mail_gunner
from src import bcrypt
import jwt


class UserModel(db.Document):
    email = db.StringField(required=True, unique=True)
    username = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    status = db.EnumField(enum=Status, default=Status.IN_ACTIVE)
    roles = db.EnumField(enum=ROLES, required=True)
    creation_date = db.DateTimeField()
    modified_date = db.DateTimeField(default=datetime.now)

    def clean(self):
        self.password = bcrypt.generate_password_hash(
            self.password).decode('utf-8')

    def save(self, *args, **kwargs):
        if not self.creation_date:
            self.creation_date = datetime.now()
        self.modified_date = datetime.now()
        return super(UserModel, self).save(*args, **kwargs)

    def update(self, *args, **kwargs):
        self.modified_date = datetime.now()
        return super(UserModel, self).update(*args, **kwargs)

    def to_dict(self):
        return dict(
            _id=str(self.pk),
            email=self.email,
            username=self.username,
            status=str(self.status.value),
            roles=str(self.roles.value),
            createdAt=self.creation_date.strftime("%m/%d/%Y, %H:%M:%S"),
            updatedAt=self.modified_date.strftime("%m/%d/%Y, %H:%M:%S")
        )

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password, attempted_password)

    def user_confirmation_mail(self, token) -> Response:
        link = request.url_root[0: -1] + f"/activate-account/activate?token={token.decode('utf-8')}"
        return mail_gunner(self.email, "User Confirmation Mail", "Store Api", link)

    @staticmethod
    def encode_auth_token(user_id: str, email: str, days=3, seconds=0):
        """ Generates the Auth Token :return: string  """
        payload = {
            'exp': datetime.utcnow() + timedelta(days=days, seconds=seconds),
            'iat': datetime.utcnow(),
            'sub': dict(user_id=user_id, email=email)
        }
        auth_token = jwt.encode(
            payload,
            CONFIG.SECRET_KEY,
            algorithm='HS256'
        )

        return dict(auth_token=auth_token)

    @staticmethod
    def compare_password(password, comparant_password):
        return safe_str_cmp(password, comparant_password)

    @classmethod
    def decode_auth_token(cls, auth_token):
        """  Decodes the auth token:param auth_token:
        :return: integer|string"""
        try:
            # get user id
            payload = jwt.decode(auth_token, CONFIG.SECRET_KEY)
            # returns id, user
            # in a bigger project caching in redis is idle if other micro services or api depend on authorisation
            if payload:
                return payload

            return False

        except jwt.ExpiredSignatureError:
            raise Exception('token has expired. Please log in again.')

        except jwt.InvalidTokenError:

            raise Exception('Invalid token. Please log in again.')
