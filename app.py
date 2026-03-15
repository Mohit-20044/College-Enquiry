from flask import Flask, render_template, request, jsonify
from chatbot_engine import get_ai_response
from database import save_chat

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"reply": "Invalid request"}), 400

    user_message = data["message"]

    # Get AI response
    bot_reply = get_ai_response(user_message)

    # Save chat to database
    save_chat(user_message, bot_reply)

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
