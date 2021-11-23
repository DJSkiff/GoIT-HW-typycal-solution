'''Типовое решение заполнения БД данными. Перед выполнением создаём
виртyальное окружение

    Будем использовать библиотеку Faker для генерации
случайных данных, в нашем случае имён студентов и преподавателей.
Больше информация - https://faker.readthedocs.io/en/master/index.html
Установка - pip install faker

    С библиотекой os вы уже знакомы.
Будем использовать для проверки существования файла БД и работы с файлом
скрипта SQL

    pandas - популярная библиотека в среде DataScience, но нас интересует
всего одна функция для генерации списка дат.
Больше информации - https://pandas.pydata.org/docs/reference/
Установка - pip install pandas'''

from random import randint
import sqlite3
import pandas as pd
import os
import faker



'''Функция создания БД, в качестве параметра -
передаем путь к фаулу с SQL скриптом'''


def create_db(path):
    # проверяем на наличие существования БД
    if not os.path.exists(f'{os.path.basename(path).split(".")[0]}.db'):
        # если БД нет - читаем файл со скриптом, переданный в параметре ф-ции
        with open(path) as f:
            sql = f.read()
# создаем соединение используя менеджер контекста
        with sqlite3.connect(
                f'{os.path.basename(path).split(".")[0]}.db') as conn:
            # создаем объект курсора
            cur = conn.cursor()
    # полностью выполняем скрипт из файла
            cur.executescript(sql)
    # подтверждаем наши действия
            conn.commit()


'''Функция генерации фейковых данных и заполнения ими БД'''


def fill_data():
    # Не все данные будут динамические. Создаем списки предметов и групп
    disciplines = ['Вища математика', 'Хімія', 'Економіка',
                   'Теоретична механіка', 'Менеджмент організацій']

    groups = ['ВВ1', 'ДД33', 'АА5']

# Создаем объект библиотеки Faker. В качестве параметра передаем локаль
# Больше - https://faker.readthedocs.io/en/master/locales.html
    fake = faker.Faker('uk-UA')
# создаём соединение, можно
    conn = sqlite3.connect('education.db')
# создаем курсор
    cur = conn.cursor()

#
    try:

        teachers = []  # создаем пустой список преподавателей

        # заполняем его случайными именами из объекта fake
        # range принимает в качестве параметра кол-во требуемых объектов
        for _ in range(3):  
            teachers.append(fake.name())

        # создаём переменную с текстом запроса для заполнения таблицы teachers
        sql_teachers = 'INSERT INTO teachers (teacher) VALUES (?)'

        # выполняем запрос используя функцию executemany объекта cursor
        # https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.executemany
        cur.executemany(sql_teachers, zip(teachers,))

        # создаём переменную с текстом запроса для заполнения таблицы disciplines
        sql_disc = 'INSERT INTO disciplines (discipline, teacher) VALUES (?, ?)'

        cur.executemany(sql_disc, zip(
            disciplines, iter(randint(1, 3) for _ in range(len(disciplines)))))

        # создаём переменную с текстом запроса для заполнения таблицы groups
        # так как для SQLite group - зарезервированное слово, берем его в [] для использования
        sql_groups = 'INSERT INTO groups ([group]) VALUES (?)'

        cur.executemany(sql_groups, zip(groups,))

        students = []  # создаем пустой список студентов

        # заполняем его случайными именами из объекта fake
        for _ in range(30):
            students.append(fake.name())

        sql_students = 'INSERT INTO students (student, [group]) VALUES (?,?)'

        cur.executemany(sql_students, zip(students, iter(randint(1, 3)
                                                         for _ in range(len(students)))))

        # для заполнения таблицы grades нам нужны даты, в которые происходит обучение
        # используем ф-цию date_range библиотеки pandas для их генерации
        # больше - https://pandas.pydata.org/docs/reference/api/pandas.date_range.html
        d_range = pd.date_range(start='2020-09-01', end='2021-05-25', freq='B')

        # создаём пустой список, в котором будем генерировать записи с оценками для каждого студента
        grades = []

        for d in d_range:  # пройдемся по каждой дате
            # рандомно выберем id одного придмета. Считаем, что в один день у нас один предмет
            r_disc = randint(1, 5)
            # допустим, что в один день могут ответить только три студента
            # выбираем троих из наших 30.
            r_students = [randint(1, 30) for _ in range(3)]
            # проходимся по списку "везучих" студентов, добавляем их в результирующий список
            # и генерируем оценку
            for student in r_students:
                grades.append((student, r_disc, d.date(), randint(1, 12)))

        sql_ratings = 'INSERT INTO grades (student, discipline, date_of, grade) VALUES (?, ?, ?, ?)'

        cur.executemany(sql_ratings, grades)

        conn.commit()

    except sqlite3.IntegrityError as e:
        print(e)

    finally:
        conn.close()


def query_1():
    with sqlite3.connect('education.db') as conn:
        cur = conn.cursor()
        sql = ''' SELECT s.student, round(avg(g.grade), 2) AS avg_grade
                  FROM grades g
                  LEFT JOIN students s ON s.id = g.student
                  GROUP BY s.id
                  ORDER BY (round(avg(g.grade), 2)) DESC
                  LIMIT 5;'''
        cur.execute(sql)
        print(cur.fetchall())


def query_2(id_discipline: int):
    with sqlite3.connect('education.db') as conn:
        cur = conn.cursor()
        sql = ''' SELECT d.discipline, s.student, round(avg(g.grade), 2) AS grade
                  FROM grades g
                  LEFT JOIN students s ON s.id = g.student
                  LEFT JOIN disciplines d ON d.id = g.discipline
                  WHERE d.id = ?
                  GROUP BY s.id, d.id
                  ORDER BY (round(avg(g.grade), 2)) DESC
                  LIMIT 1;'''
        cur.execute(sql, (id_discipline,))
        print(cur.fetchall())


def query_3(id_discipline: int):
    with sqlite3.connect('education.db') as conn:
        cur = conn.cursor()
        sql = ''' SELECT d.discipline, gr.[group], round(avg(g.grade), 2) AS grade
                  FROM grades g
                  LEFT JOIN students s ON s.id = g.student
                  LEFT JOIN disciplines d ON d.id = g.discipline
                  LEFT JOIN [groups] gr ON gr.id = s.[group]
                  WHERE d.id = ?
                  GROUP BY gr.id
                  ORDER BY (round(avg(g.grade), 2)) DESC'''
        cur.execute(sql, (id_discipline,))
        print(cur.fetchall())


def query_4():
    with sqlite3.connect('education.db') as conn:
        cur = conn.cursor()
        sql = '''SELECT round(avg(grade),2) AS avg_grade
                 FROM grades
              '''
        cur.execute(sql)
        print(cur.fetchall())

def query_5(id_teacher:int):
    with sqlite3.connect('education.db') as conn:
        cur = conn.cursor()
        sql = '''SELECT t.teacher, d.discipline
                 FROM teachers t
                 LEFT JOIN disciplines d ON d.teacher = t.id
                 WHERE t.id = ?'''
        cur.execute(sql, (id_teacher,))
        print(cur.fetchall())
        
        
def query_6(id_group:int):
    with sqlite3.connect('education.db') as conn:
        cur = conn.cursor()
        sql = '''SELECT g.[group], s.student
                 FROM students s
                 LEFT JOIN [groups] g ON g.id = s.[group]
                 WHERE g.id = ?'''
        cur.execute(sql, (id_group,))
        print(cur.fetchall())
        
if __name__ == '__main__':
    create_db('education.sql')
    fill_data()
    query_1()
    query_2(2)
    query_3(1)
    query_4()
    query_5(3)
    query_6(2)
