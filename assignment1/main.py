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
@app.route("/location-form", methods=["GET", "POST"])
def location_form():
    # Handle POST request
    if request.method == "POST":
        country = request.form.get("country")
        city = request.form.get("city")
        return """
            <p>Location: {}, {}</p>
        """.format(city, country)


    # Handle GET request (HTML form element)
    return """
        <form method="POST">
          <div>
            <label>City:</label>
            <input type="text" name="city" placeholder="Please input your city" />
          </div>
          <div>
            <label>Country:</label>
            <input type="text" name="country" placeholder="Please input your country" />
          </div>
          <input type="submit" value="Submit" />
        </form>
    """
    


if __name__ == "__main__":
    app.run(debug=True)
