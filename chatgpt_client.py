from revChatGPT.V1 import Chatbot
from auth_client import AuthClient


class ChatGPTClient:
    def __init__(self) -> None:
        tokens = AuthClient().get_tokens()
        """
        "text-davinci-002-render-sha" - Default (faster)
        "text-davinci-002-render-paid" - Legacy
        """
        self.chatbot = Chatbot(
            config={
                "access_token": tokens.get("access_token"),
                "session_token": tokens.get("session_token"),
                "paid": False,
            }
        )

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
    c = ChatGPTClient()
    """
    [
        {
            "id": "b46b045d-c893-4ec6-b40f-4013484e096c",
            "title": "INTJ Personality Description",
            "create_time": "2023-02-26T09:16:16.467803"
        }
    ]
    """
    conversations = c.chatbot.get_conversations(offset=0, limit=2)
    print(conversations)
