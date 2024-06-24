import jwt
import datetime
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Access the environment variables
secret_key = os.getenv('SECRET_KEY')


print(f"SECRET_KEY: {secret_key}")


def jwt_encode(user_id, username):
    SECRET_KEY = '123456789'
    payload = {
        'user_id': user_id,
        'username': username,
        'exp': datetime.datetime.now() + datetime.timedelta(hours=24)
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    return token

def jwt_decode(token):
    SECRET_KEY = '123456789'
    try:
        # Decode the token
        decoded_payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])

        return decoded_payload
    except jwt.ExpiredSignatureError:
        print("Token has expired")
    except jwt.InvalidTokenError:
        print("Invalid token")

jwt_decode(jwt_encode(1, "123"))

