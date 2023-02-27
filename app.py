from flask import Flask, request, jsonify, Blueprint
from chatgpt_client import ChatGPTClient
from auth_client import AuthClient

# Create a new Flask application
app = Flask(__name__)

api_v1 = Blueprint("api_v1", __name__, url_prefix="/api/v1")

client = ChatGPTClient()


def resp_success(data=None):
    return jsonify({"success": True, "data": data})


def resp_error(message=None):
    return jsonify({"success": False, "message": message})


@app.route("/")
def hello():
    return "Hello, World!"


@api_v1.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()

    prompt = data.get("prompt")
    conversation_id = data.get("conversation_id")
    parent_id = data.get("parent_id")

    if prompt is None or not prompt:
        return resp_error(f"prompt={prompt}")

    response = client.ask(prompt, conversation_id, parent_id)

    return jsonify(response)


@api_v1.route("/auth", methods=["POST"])
def auth():
    AuthClient().start()
    return resp_success()


@api_v1.route("/conversations", methods=["GET"])
def get_conversations():
    offset = request.args.get("offset", None)
    limit = request.args.get("limit", None)

    def check_is_valid(v: str):
        if v is not None:
            if v is not v.isdigit() or int(v) < 0:
                return False
        return True

    if not check_is_valid(offset) or not check_is_valid(limit):
        return resp_error(f"offset={offset}, limit={limit}"), 400

    conversations = client.chatbot.get_conversations(offset, limit)
    return resp_success(conversations)


@api_v1.route("/messages", methods=["GET"])
def get_msg_history():
    conversation_id = request.args.get("conversation_id")

    if conversation_id is None or not conversation_id:
        return resp_error(f"conversation_id={conversation_id}")

    messages = client.chatbot.get_msg_history(convo_id=conversation_id)
    return resp_success(messages)


def gen_title():
    pass


@api_v1.route("/conversation", methods=["DELETE"])
def delete_conversation():
    conversation_id = request.args.get("conversation_id")
    if conversation_id is None or not conversation_id:
        return resp_error(f"conversation_id={conversation_id}"), 400

    client.chatbot.delete_conversation(convo_id=conversation_id)
    return resp_success()


app.register_blueprint(api_v1)

# Run the application
if __name__ == "__main__":
    print(app.url_map)
    app.run()
