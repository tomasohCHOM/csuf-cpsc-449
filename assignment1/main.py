from flask import Flask, jsonify, request

app = Flask(__name__)


# GET endpoint that greets the user
@app.route("/", methods=["GET"])
def greet():
    return "Hello! My name is Tomas Oh", 200


# POST endpoint that gets data from the JSON request body and returns it back
@app.route("/user", methods=["POST"])
def user():
    data = request.json
    if not data or len(data) < 5:
        return (
            jsonify({"error": "The JSON object must contain at least 5 fields."}),
            400,
        )
    return jsonify(data), 200


# GET and POST endpoint for the user's location (city, country)
@app.route("/ide", methods=["GET", "POST"])
def location_form():
    ide = "VI" if request.method == "POST" else "Emacs"
    return ide, 200


if __name__ == "__main__":
    app.run(debug=True)
