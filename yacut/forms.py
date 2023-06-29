from flask_wtf import FlaskForm
from wtforms import SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional


class LinkForm(FlaskForm):
    original_link = URLField(
        "Длинная ссылка ссылка",
        validators=[DataRequired(message="Обязательное поле")],
    )
    custom_id = URLField(
        "Ваш вариант короткой ссылки",
        validators=[Length(1, 256), Optional()],
    )

    submit = SubmitField("Добавить")
