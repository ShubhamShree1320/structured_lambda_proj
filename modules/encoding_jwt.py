from dependencies import jwt
def encoding_jwt(payload,secret_key):

    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return(token)