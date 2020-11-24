from bson import ObjectId
from flask import Blueprint, request, make_response, jsonify
from models.client import PyMongoParser, news_collection, authors_collection
from validators.author import AuthorValidator
from validators.news import NewsValidator
from datetime import datetime

news = Blueprint(
    "news",
    __name__,
    url_prefix="/api/news"
)


@news.route("/", methods=["GET"])
def get_news():
    id = request.args.get("id")
    title = request.args.get("title")
    author_name = request.args.get("author")
    author_id = request.args.get("author_id")

    news = []

    if id:
        news_obj_id = ObjectId(id)
        news = news_collection.find_one({"_id": news_obj_id})

    if author_id:
        author_obj_id = ObjectId(author_id)
        found_author = authors_collection.find_one({"_id": author_obj_id})
        news = [result for result in news_collection.find({"author": {"name": found_author.get("name")}})]

    if author_name:
        news = [result for result in news_collection.find({"author": {"name": author_name}})]
        print(news)

    if title:
        news = news_collection.find_one({"title": title})

    if not news:
        news = [result for result in news_collection.find()]

    return make_response(jsonify({"success": PyMongoParser.parse_json(news)}), 200)


@news.route("/create", methods=["POST"])
def add_news():

    if not request.json:
        return make_response(jsonify({"error": "empty json body"}), 400)

    title = request.json.get('title')
    content = request.json.get('content')
    author_id = request.json.get('author_id')

    title, errors = NewsValidator.title_validators(title)
    content, errors = NewsValidator.content_validators(content)
    author_id, errors = AuthorValidator.author_key_validators(author_id)

    if len(errors) > 0:
        print(errors)
        return make_response(jsonify({"error": errors}), 400)

    obj_id = ObjectId(author_id)
    author = authors_collection.find_one({"_id": obj_id})
    if not author:
        return make_response(jsonify({"error": "author with id {} does not exist".format(author_id)}), 400)

    if news_collection.find_one({"title": title}):
        return make_response(jsonify({"error": "News with title {} already exists".format(title)}), 400)

    data = {
        "title": title,
        "content": content,
        "created_at": datetime.now(),
        "author": author
    }
    added_news = news_collection.insert_one(data)

    return make_response(jsonify({"success": PyMongoParser.parse_json(added_news.inserted_id)}), 201)


@news.route("/update", methods=["POST"])
def update_news():

    if not request.json:
        return make_response(jsonify({"error": "empty json body"}), 400)

    title = request.json['title']
    content = request.json['content']
    author_id = request.json['author_id']

    title, errors = NewsValidator.title_validators(title)
    content, errors = NewsValidator.content_validators(content)
    author_id, errors = AuthorValidator.author_key_validators(author_id)

    if len(errors) > 0:
        print(errors)
        return make_response(jsonify({'error': errors}), 400)

    data = {
        "title": title,
        "content": content,
        "author_id": author_id,
        "created_at": datetime.now()
    }

    try:
        existing_new = news_collection.find_one({"title": title})
    except:
        existing_new = None

    if not existing_new:
        return make_response(jsonify({"error": "News with title '{}' not found".format(title)}), 404)

    try:
        if existing_new and existing_new.title == title:
            data.update({"id": existing_new.id})
            # updated_new = News(**data).save()
            return make_response(jsonify({"success": updated_new}), 201)
    except Exception as error:
        return make_response(jsonify({"error": "error on updating: {}".format(error)}), 400)


@news.route("/delete", methods=["DELETE"])
def delete_news():
    id = request.args.get('id')
    title = request.args.get('title')

    news = None

    if id:
        obj_id = ObjectId(id)
        news = news_collection.find_one({"_id": obj_id})
        news_collection.delete_one(news) if news else None

    if title:
        news = news_collection.find_one({"title": title})
        news_collection.delete_one(news) if news else None

    if not news:
        return make_response(jsonify({"error": "News not found or already deleted"}), 404)

    return make_response(jsonify({"success": "deleted news {}".format(news.get("_id"))}), 202)
