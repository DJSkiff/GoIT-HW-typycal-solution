# Учимся создавать БД и писать запросы

В примере будет использована стандартная библиотека `python` - `sqlite3` и сторонний пакет `Faker` для генерации случайных данных.

1. Создаем папку с проектом.
2. Создаем виртуальное окружение и активируем его.
3. Создаем файл со скриптами создания таблиц БД на языке SQL (т.к. SQLite это БД "в одном файле" то сама она создастся при первом подключении к ней).
4. Перейдем к "физическому" созданию БД. В файле `create_db.py` содержится минимум строк, для создания БД и таблиц в ней.
5. Теперь нужно наполнить нашу БД данными, для этого используем пакет **Faker** (`pip install faker`).Наша база будет содержать данные о 3-х компаниях, в которых в общем количестве работает 30 человек. Персонал рандомно разбросан по 5-ти должностям. А также ми имеем статистику по выплаченной зарплате сотрудникам в течении года.
6. После заполнения БД напишем функцию которая будет возвращать список данных в ответ на переданный ей текст SQL-запроса. Сами запросы будем писать в файлах `.sql`.