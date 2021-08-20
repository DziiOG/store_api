from flask import Response
from typing import Dict

def success( message: str, statusCode=200):
    return {'message': message, 'statusCode': statusCode}

def successWithData(data, message, statusCode=200):
    return {'statusCode': statusCode, 'message': message, 'data': data}

def error(message, statusCode=400):
    return {'statusCode': statusCode, 'message': message}    
