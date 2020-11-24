from flask import Flask, jsonify, make_response
from flask.json import JSONEncoder
from authors.authors import authors
from news.news import news

app = Flask(__name__)

app.secret_key = "some big secret key to modify later..."
app.config['JSON_AS_ASCII'] = False
app.json_encoder = JSONEncoder
app.register_blueprint(news)
app.register_blueprint(authors)


@app.route("/")
@app.route("/api")
def index():
    return make_response(jsonify({"success": "our API is working!"}), 200)


@app.errorhandler(404)
def not_found(e):
    return make_response(jsonify({"error": "route not found"}), 404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
