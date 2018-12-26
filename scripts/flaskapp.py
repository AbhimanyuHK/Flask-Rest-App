import json

from flask import Flask, request

from scripts.dao.database import Database as db
from scripts.utils.utils import date_converter

app = Flask(__name__)


@app.route('/all', methods=["GET"])
def get_all_objects():
    all_objects = json.dumps(db().get_all(), default=date_converter)
    return str(all_objects)


@app.route('/create', methods=["POST"])
def create_object():
    body = request.data
    count = db().insert(json.loads(body))
    return "Inserted" + str(count)


@app.route('/delete/<id>', methods=["DELETE"])
def delete_object(id):
    return "Deleted " + str(db().delete_by_id(id)) + " Rows"


@app.route('/update/<id>', methods=["POST"])
def update_object(id):
    body = request.data
    count = db().update(id, json.loads(body))
    return str({"id": id, "body": json.loads(body), "count": count})


@app.route('/get/<id>', methods=["GET"])
def get_object(id):
    return str(json.dumps(db().get_by_id(id), default=date_converter))


if __name__ == '__main__':
    app.run()
