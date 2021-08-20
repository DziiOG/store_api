from marshmallow import Schema, fields


class ItemBodyValidation(Schema):
    name = fields.String(required=True)
    price = fields.Float(required=True)


class ItemPatchBodyValidation(Schema):
    name = fields.String()
    price = fields.Float()
    creation_date = fields.Date()
    modified_date = fields.Date()


class ItemParamsValidation(Schema):
    name = fields.String()
    price = fields.Float()
