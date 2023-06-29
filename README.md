# YaCut — Сократить ссылку

Сервис укорачивания ссылок.
Его назначение — ассоциировать длинную пользовательскую ссылку с короткой,
которую предлагает сам пользователь или предоставляет сервис.

Клонировать репозиторий и перейти в него в командной строке:

```
git clone 
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt

```
1. В корне проекта создай .env файл
      FLASK_APP=yacut
      FLASK_ENV=development
      DATABASE_URI=sqlite:///db.sqlite3
      SECRET_KEY=YOUR_SECRET_KEY
2. ```flask run```


## Использование

### API
Запросы:
  - **POST** `/api/id/`
- **GET** `/api/id/{short_id}/`
API (Docs:(openapi.yml))