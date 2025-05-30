from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def handle_get():
    return "Server is running!"

@app.route('/', methods=['POST'])
def handle_post():
    try:
        data = request.get_json()

        if data.get("request_type") == "customerlogin":
            response = requests.post(
                "https://your-secret-api.com/login",
                json={
                    "user": data.get("user"),
                    "hwid": data.get("hwid")
                }
            )
            return (response.content, response.status_code, response.headers.items())

        return jsonify({"error": "Unknown request_type"}), 400

    except Exception as e:
        return jsonify({"error": True, "message": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
