from modules.decoding_jwt import decoding_with_jwt
from modules.encoding_jwt import encoding_jwt
import datetime
def lambda_handler(event,context):
    # Define a secret key (keep it safe and secure)
    secret_key = 'your_secret_key'

    # Create a payload (claims)
    payload = {
        'user_id': 123,
        'username': 'john_doe',
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expires in 1 hour
    }
    token=encoding_jwt(payload,secret_key)
    print(token)
    original_data=decoding_with_jwt(token,secret_key)
    print(original_data)
