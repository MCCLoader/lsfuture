from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def handle_get():
    return "Server is running!"

@app.route('/api', methods=['POST'])
def handle_post():
    try:
        data = request.get_json()

        print(data.get("temp"))

        return data.get("temp")

    except Exception as e:
        return jsonify({"error": True, "message": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
