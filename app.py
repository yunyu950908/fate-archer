from flask import Flask, request, jsonify
from chatgpt_client import ChatGPTClient
from auth_client import AuthClient

# Create a new Flask application
app = Flask(__name__)

# Define a route and a view function


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/api/ask", methods=["POST"])
def ask():
    data = request.get_json()

    prompt = data.get("prompt")
    conversation_id = data.get("conversation_id")
    parent_id = data.get("parent_id")

    client = ChatGPTClient()
    response = client.ask(prompt, conversation_id, parent_id)

    return jsonify(response)


@app.route("/api/auth", methods=["POST"])
def auth():
    AuthClient().start()
    return jsonify({"success": True})


# Run the application
if __name__ == "__main__":
    app.run()
