import json
import os
import sys
import redis
from datetime import datetime
from OpenAIAuth import Authenticator

email_address = os.environ.get('email_address')
password = os.environ.get('password')
proxy = os.environ.get('proxy')


class AuthClient:
    def __init__(self):
        self.access_token_key = "openai:access_token"
        self.session_token_key = "openai:session_token"
        self.r = redis.Redis(host='localhost', port=6379, db=0)

    def start(self):
        if email_address is None or password is None:
            print(f"{datetime.now()}\tInvalid email_address or password")
            sys.exit(1)

        auth = Authenticator(
            email_address,
            password,
            proxy
        )
        auth.begin()

        self.set_tokens(
            access_token=auth.access_token,
            session_token=auth.session_token
        )
        print('auth success finished')
        print()

    def set_tokens(self, access_token: str, session_token: str):
        self.r.set(self.access_token_key, access_token)
        self.r.set(self.session_token_key, session_token)

    def get_tokens(self):
        access_token = self.r.get(self.access_token_key).decode('utf-8')
        session_token = self.r.get(self.session_token_key).decode('utf-8')
        return {
            "access_token": access_token,
            "session_token": session_token
        }


if __name__ == '__main__':
    AuthClient().start()
