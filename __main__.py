import json
import os
import sys
from datetime import datetime
from OpenAIAuth import Authenticator
from revChatGPT.V1 import Chatbot

email_address = os.environ.get('email_address')
password = os.environ.get('password')
proxy = os.environ.get('proxy')


def auth():
    if email_address is None or password is None:
        print(f"{datetime.now()}\tInvalid email_address or password")
        sys.exit(1)

    user = Authenticator(
        email_address,
        password,
        proxy
    )
    user.begin()
    user_info = {
        "access_token": user.access_token,
        "session_token": user.session_token
    }
    print(f"{json.dumps(user_info, indent=4)}")
    return user_info


if __name__ == '__main__':
    # auth_info = auth()
    user_info = auth()

    chatbot = Chatbot(config={
        "proxy": proxy,
        "access_token": user_info["access_token"],
        "session_token": user_info["session_token"]
    })

    print("Chatbot: ")
    prev_text = ""
    for data in chatbot.ask(
        "写一段冒泡排序",
    ):
        message = data["message"][len(prev_text):]
        print(message, end="", flush=True)
        prev_text = data["message"]
    print()
    # print(f"${datetime.now()}\t{auth_info}")
    print(f"{datetime.now()}\tall done")
    #  export https_proxy=http://127.0.0.1:8888;export http_proxy=http://127.0.0.1:8888;export all_proxy=socks5://127.0.0.1:8889
