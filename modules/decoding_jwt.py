from dependencies import jwt


def decoding_with_jwt(token, secret_key):
    try:
        # Decode the JWT
        decoded_payload = jwt.decode(token, secret_key, algorithms=["HS256"])
        return f"Decoded Payload: {decoded_payload}"
    except jwt.ExpiredSignatureError:
        print("Token has expired.")
    except jwt.InvalidTokenError:
        print("Invalid token.")

