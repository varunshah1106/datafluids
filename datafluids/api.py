from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
from config import config
from bson import json_util

import datetime
import json

app = Flask(__name__)
app.config.update(config)
mongo = PyMongo(app)


@app.route('/', methods=['GET'])
def root():
    folderpath = mongo.db.get_collection('folderpath')
    result = []
    for d in folderpath.find({}):
        result.append(d)
    return jsonify({
        "result": [json.loads(json.dumps(
            item, indent=4, default=json_util.default)) for item in result]
    })


if __name__ == '__main__':
    app.run(debug=True)
