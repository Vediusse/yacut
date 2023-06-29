import random
import re
import string
from datetime import datetime

from sqlalchemy.orm import validates
from validators import url

from . import db, app
from .errors_handlers import InvalidAPIUsage


def get_unique_link():
    letters = string.ascii_lowercase
    short = "".join(random.sample(letters, app.config["SHORT_URL_LENGTH"]))
    short_urls_in_database = URLMap.query.with_entities(URLMap.short).all()
    while (short,) in short_urls_in_database:
        short = "".join(random.sample(letters, app.config["SHORT_URL_LENGTH"]))

    return short


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.Text, nullable=False)
    short = db.Column(
        db.String(app.config["MAX_LENGTH"]),
        unique=True,
        default=get_unique_link,
    )
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    @validates("original")
    def validate_original(self, key, value):
        assert url(value) is True
        return value

    @validates("short")
    def validate_short(self, key, value):
        message = "Указано недопустимое имя для короткой ссылки"
        if re.findall(app.config["REGEX"], str(value)):
            raise InvalidAPIUsage(message)
        if len(str(value)) > 16:
            raise InvalidAPIUsage(message)
        return value
