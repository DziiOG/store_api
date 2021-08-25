



from marshmallow import Schema, fields


class StoreBodyValidation(Schema):
    name = fields.String(required=True)
    items = fields.List(fields.String())


class StorePatchBodyValidation(Schema):
    name = fields.String(required=True)
    items = fields.List(fields.String())
    creation_date = fields.Date()
    modified_date = fields.Date()


class StoreParamsValidation(Schema):
    name = fields.String()
    item = fields.String()
