# This is a sample Python script.

from jwt_folder import (
    my_jwt_encoder
)


def encode_(msg):
    token = my_jwt_encoder.get_jwt_encode("key123", "value_123")
    return token

def decode_(token):
    token = my_jwt_encoder.get_jwt_decode(token)
    return token


# # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    token = encode_("msg")
    decode_(token)
