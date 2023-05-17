from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import os

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

@app.route('/')
@cross_origin()
def index():
    return "<span>He he :)</span>"


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
