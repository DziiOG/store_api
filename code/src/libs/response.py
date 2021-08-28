from flask import Response
from typing import Dict


def success(message: str, statusCode: int = 200) -> Dict:
    return {'message': message, 'statusCode': statusCode}


def successWithData(data, message: str, statusCode: int = 200) -> Dict:
    return {'statusCode': statusCode, 'message': message, 'data': data}


def error(message: str or Dict, statusCode: int = 400) -> Dict:
    return {'statusCode': statusCode, 'message': message}

def unauthorized() -> Dict:
    return {'statusCode': 401, 'message': "Unauthorized"}

def forbidden() -> Dict:
    return {'statusCode': 403, 'message': "Forbidden"}