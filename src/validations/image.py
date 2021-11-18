from marshmallow import Schema, fields

class FileStorageField(fields.Field):
    default_error_messages= {
        'invalid': 'Not valid image'
    }
    def _deserialize(self, value, attr, data)->str:
        if value is None:
            return None

        if not isinstance(value, str):
            self.fail('invalid')

        return value

class ImageSchema(Schema):
    image = FileStorageField(required=True)