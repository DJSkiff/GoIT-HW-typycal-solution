# Flask + SQLAlchemy + Jinja2

В этом ДЗ мы с вами реализуем простую систему управления заметками с использованием популярного фреймворка [**Flask**](https://flask.palletsprojects.com/en/2.0.x/).

Для доступа к БД будем использовать ORM подход на основе [**SQLAlchemy**](https://www.sqlalchemy.org/) с которым вы уже знакомы.

Вывод данных будем делать с использованием "шаблонизатора" [**Jinja2**](https://lectureswww.readthedocs.io/6.www.sync/2.codding/3.templates/jinja2.html) который используется во многих популярных web-фреймворках на Python.

Первым делом создадим виртуальное окружение `python -m venv venv`

Далее установим нужные нам пакеты:

- `pip install flask`
- `pip install sqlalchemy`

Создадим первый файл и назовем его **app.py** - это будет основной файл нашего приложения. Минимально требуемый код для запуска сервера будет выглядеть так:

```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world"

if __name__ == "__main__":
    app.run()
```

Далее создадим файл **db.py** - в котором будем хранить данные которые нам потребуються для подключения к нашей БД.

Модели наших классов опишем в файле **models.py**. Для создания БД и добавления туда таблиц нам нужно будет запустить на выполнение файл **models.py** из консоли `python models.py`
