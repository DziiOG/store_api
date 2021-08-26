



from marshmallow import Schema, fields


class StoreBodyValidation(Schema):
    name = fields.String(required=True)
    items = fields.List(fields.String())


class StorePatchBodyValidation(Schema):
    name = fields.String(required=True)
    creation_date = fields.Date()
    modified_date = fields.Date()

class StoreItemPatchBodyValidation(Schema):
    items = fields.List(fields.String(required=True))


class StoreParamsValidation(Schema):
    name = fields.String()
    item = fields.String()
