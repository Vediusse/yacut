import re

from flask_wtf import FlaskForm
from sqlalchemy.orm import validates
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional

from . import app
from .errors_handlers import InvalidAPIUsage


class LinkForm(FlaskForm):
    original_link = URLField(
        "Длинная ссылка ссылка",
        validators=[DataRequired(message="Обязательное поле")],
    )
    custom_id = URLField(
        "Ваш вариант короткой ссылки", validators=[Length(1, 256), Optional()]
    )

    submit = SubmitField("Добавить")

    @validates("custom_id")
    def validate_short(self, key, value):
        message = "Указано недопустимое имя для короткой ссылки"
        if re.findall(app.config["REGEX"], str(value)):
            raise InvalidAPIUsage(message)
        if len(str(value)) > 16:
            raise InvalidAPIUsage(message)
        return value
