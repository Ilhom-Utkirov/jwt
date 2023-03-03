import jwt
import os
from os.path import join, dirname
from dotenv import load_dotenv
import time

dotenv_path = join(dirname(__file__), 'application.env')
load_dotenv(dotenv_path)
secret_key = os.environ['security_password']
print(secret_key)


def get_jwt_encode(key_, value_):
    # use any word to encode
    ps = jwt.encode({key_: value_}, secret_key, algorithm="HS256")
    print(f'Encoded code\n{ps}')
    return ps


def get_jwt_decode(token):
    dc = jwt.decode(token, secret_key, algorithms=["HS256"])
    print(f'Decoded code\n{dc}')
