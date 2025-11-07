from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Provided test API key
API_KEY = "AIzaSyDSKBupwR_jNNUTFeodQkOl26LlA0gjxcU"
# Gemini endpoint
ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

@app.route("/generate", methods=["POST", "GET"])
def generate():
    if request.method == "POST":
        data = request.get_json()
        prompt = data.get("prompt", "")
        debug = data.get("debug", False)
    else:
        prompt = request.args.get("prompt", "")
        debug = request.args.get("debug", "false").lower() == "true"

    if not prompt:
        return jsonify({"error": "Please provide a prompt"}), 400

    headers = {"Content-Type": "application/json"}
    payload = {"contents": [{"parts": [{"text": prompt}]}]}

    try:
        response = requests.post(f"{ENDPOINT}?key={API_KEY}", headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()

        # Extract model response
        reply = result["candidates"][0]["content"]["parts"][0]["text"]

        if debug:
            return jsonify({"response": reply, "raw": result})
        return jsonify({"response": reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
