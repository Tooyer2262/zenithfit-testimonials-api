from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

DATA_FILE = "reviews.json"

def load_reviews():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_review(new_review):
    reviews = load_reviews()
    reviews.append(new_review)
    with open(DATA_FILE, "w") as f:
        json.dump(reviews, f)

# ✅ Add this route so the root URL doesn't show a 404
@app.route("/")
def home():
    return "ZenithFIT Testimonials API is running."

@app.route("/api/testimonials", methods=["GET"])
def get_reviews():
    return jsonify(load_reviews()[-10:])  # Only return the latest 10

@app.route("/api/testimonials", methods=["POST"])
def post_review():
    data = request.get_json()
    if "name" in data and "rating" in data and "message" in data:
        save_review({
            "name": data["name"],
            "rating": data["rating"],
            "message": data["message"]
        })
        return jsonify({"status": "success"}), 200
    return jsonify({"status": "error"}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)