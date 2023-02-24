from revChatGPT.V1 import Chatbot
from auth_client import AuthClient


class ChatGPTClient:
    def __init__(self) -> None:
        tokens = AuthClient().get_tokens()
        self.chatbot = Chatbot(config={
            "access_token": tokens.get("access_token"),
            "session_token": tokens.get("session_token"),
            "paid": True
        })

    """
    {
        "message": "你好！有什么我可以帮助你的？",
        "conversation_id": "1cec53c9-6cf0-4d78-9b9c-2283c5a970ba",
        "parent_id": "6c8f5095-2d7f-4022-bc43-e1f69859591c"
    }
    """

    def ask(self, prompt: str, conversation_id: str = None, parent_id: str = None):
        for data in self.chatbot.ask(prompt, conversation_id, parent_id):
            pass
        return data


if __name__ == "__main__":
    data = ChatGPTClient().ask("你好")
    print(data)
