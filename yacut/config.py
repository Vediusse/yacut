import os
import re

SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite3"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.getenv("SECRET_KEY", default="YOUR_SECRET_KEY")
SHORT_URL_LENGTH = 6
MAX_LENGTH = 128
REGEX = re.compile(r"[.,\-!?$#а-яА-ЯёЁ\s]")
