from urllib.parse import urljoin

from flask import jsonify, request

from . import app, db
from .errors_handlers import InvalidAPIUsage, InvalidUrl
from .models import URLMap


@app.route("/api/id/<string:short>/", methods=["GET"])
def get_url(short):
    url = URLMap.query.filter_by(short=short).first()
    if url is None:
        raise InvalidUrl("Указанный id не найден")
    return jsonify({"url": url.original}), 200


@app.route("/api/id/", methods=["POST"])
def post_url():
    data = request.get_json()
    if data is None:
        raise InvalidAPIUsage("Отсутствует тело запроса")
    elif "url" not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')

    original = data["url"]
    url = URLMap(original=original)
    if "custom_id" in data:
        short = data["custom_id"]
        if URLMap.query.filter_by(short=short).first():
            raise InvalidAPIUsage(f'Имя "{short}" уже занято.')

        url.short = short
        db.session.add(url)
        db.session.commit()
        result = dict(
            url=url.original,
            short_link=urljoin(request.url_root, url.short),
        )
        return jsonify(result), 201

    db.session.add(url)
    db.session.commit()
    result = dict(
        url=url.original,
        short_link=urljoin(request.url_root, url.short),
    )
    return jsonify(result), 201
