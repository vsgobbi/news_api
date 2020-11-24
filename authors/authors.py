from bson import ObjectId
from flask import Blueprint, request, make_response, jsonify
from datetime import datetime
from validators.author import AuthorValidator
from models.client import PyMongoParser, authors_collection

authors = Blueprint(
    "authors",
    __name__,
    url_prefix="/api/authors"
)


@authors.route("/", methods=["GET"])
def get_authors():
    id = request.args.get('id')
    author = request.args.get('author')

    authors = []

    if id:
        obj_id = ObjectId(id)
        authors = authors_collection.find_one({"_id": obj_id})

    if author:
        authors = authors_collection.find_one({"name": author})

    if not authors:
        authors = [author for author in authors_collection.find()]

    return make_response(jsonify({"success": PyMongoParser.parse_json(authors)}), 200)


@authors.route("/create", methods=["POST"])
def add_author():
    name = request.json['name']
    city = request.json['city']

    author_name, errors = AuthorValidator.author_name_validators(name)

    if len(errors) > 0:
        print(errors)
        return make_response(jsonify({'result': errors}), 400)

    data = {
        "name": name,
        "city": city,
        "created_at": datetime.now()
    }

    existing_author = authors_collection.find_one({"name": name})

    if existing_author:
        print("Author {} já existe".format(existing_author))
        return make_response(jsonify({"error": "Author {} already exists".format(name)}), 400)

    new_author = authors_collection.insert_one(data)
    return make_response(jsonify({"success": PyMongoParser.parse_json(new_author.inserted_id)}), 201)
