import sqlite3


"""5 студентов с наибольшим средним баллом по всем предметам"""


def query_1():
    with sqlite3.connect("education.db") as conn:
        cur = conn.cursor()
        sql = """ SELECT s.student, round(avg(g.grade), 2) AS avg_grade
                  FROM grades g
                  LEFT JOIN students s ON s.id = g.student
                  GROUP BY s.id
                  ORDER BY (round(avg(g.grade), 2)) DESC
                  LIMIT 5;"""
        cur.execute(sql)
        print(cur.fetchall())


"""1 студент с наивысшим средним баллом по одному предмету."""


def query_2(id_discipline: int):
    with sqlite3.connect("education.db") as conn:
        cur = conn.cursor()
        sql = """ SELECT d.discipline, s.student, round(avg(g.grade), 2) AS grade
                  FROM grades g
                  LEFT JOIN students s ON s.id = g.student
                  LEFT JOIN disciplines d ON d.id = g.discipline
                  WHERE d.id = ?
                  GROUP BY s.id, d.id
                  ORDER BY (round(avg(g.grade), 2)) DESC
                  LIMIT 1;"""
        cur.execute(sql, (id_discipline,))
        print(cur.fetchall())


"""Cредний балл в группе по одному предмету."""


def query_3(id_discipline: int):
    with sqlite3.connect("education.db") as conn:
        cur = conn.cursor()
        sql = """ SELECT d.discipline, gr.[group], round(avg(g.grade), 2) AS grade
                  FROM grades g
                  LEFT JOIN students s ON s.id = g.student
                  LEFT JOIN disciplines d ON d.id = g.discipline
                  LEFT JOIN [groups] gr ON gr.id = s.[group]
                  WHERE d.id = ?
                  GROUP BY gr.id
                  ORDER BY (round(avg(g.grade), 2)) DESC"""
        cur.execute(sql, (id_discipline,))
        print(cur.fetchall())


"""Средний балл в потоке."""


def query_4():
    with sqlite3.connect("education.db") as conn:
        cur = conn.cursor()
        sql = """SELECT round(avg(grade),2) AS avg_grade
                 FROM grades
              """
        cur.execute(sql)
        print(cur.fetchall())


"""Какие курсы читает преподаватель."""


def query_5(id_teacher: int):
    with sqlite3.connect("education.db") as conn:
        cur = conn.cursor()
        sql = """SELECT t.teacher, d.discipline
                 FROM teachers t
                 LEFT JOIN disciplines d ON d.teacher = t.id
                 WHERE t.id = ?"""
        cur.execute(sql, (id_teacher,))
        print(cur.fetchall())


"""Список студентов в группе"""


def query_6(id_group: int):
    with sqlite3.connect("education.db") as conn:
        cur = conn.cursor()
        sql = """SELECT g.[group], s.student
                 FROM students s
                 LEFT JOIN [groups] g ON g.id = s.[group]
                 WHERE g.id = ?"""
        cur.execute(sql, (id_group,))
        print(cur.fetchall())


"""Оценки студентов в группе по предмету."""


def query_7(id_discipline: int, id_group: int):
    with sqlite3.connect("education.db") as conn:
        cur = conn.cursor()
        sql = """SELECT d.discipline, gr.[group], s.student, g.date_of, g.grade
                  FROM grades g
                  LEFT JOIN students s ON s.id = g.student
                  LEFT JOIN disciplines d ON d.id = g.discipline
                  LEFT JOIN [groups] gr ON gr.id = s.[group]
                  WHERE d.id = ? AND gr.id = ?"""
        cur.execute(sql, (id_discipline, id_group))
        print(cur.fetchall())


"""Оценки студентов в группе по предмету на последнем занятии."""


def query_8(id_discipline: int, id_group: int):
    with sqlite3.connect("education.db") as conn:
        cur = conn.cursor()
        sql = """SELECT d.discipline, gr.[group], s.student, g.date_of, g.grade
                  FROM grades g
                  LEFT JOIN students s ON s.id = g.student
                  LEFT JOIN disciplines d ON d.id = g.discipline
                  LEFT JOIN [groups] gr ON gr.id = s.[group]
                  WHERE d.id = ? AND gr.id = ? AND g.date_of = 
                  (SELECT MAX(grades.date_of) FROM grades WHERE grades.discipline = d.id)"""
        cur.execute(sql, (id_discipline, id_group))
        print(cur.fetchall())


"""Список курсов, которые посещает студент."""


def query_9(id_student: int):
    with sqlite3.connect("education.db") as conn:
        cur = conn.cursor()
        sql = """SELECT DISTINCT s.student, d.discipline 
                 FROM grades g
                 LEFT JOIN students s ON s.id = g.student
                 LEFT JOIN disciplines d ON d.id = g.discipline 
                 WHERE g.student = ?"""
        cur.execute(sql, (id_student,))
        print(cur.fetchall())


"""Список курсов, которые студенту читает преподаватель."""


def query_10(id_student: int, id_teacher: int):
    with sqlite3.connect("education.db") as conn:
        cur = conn.cursor()
        sql = """SELECT DISTINCT s.student, t.teacher, d.discipline 
                 FROM grades g
                 LEFT JOIN students s ON s.id = g.student
                 LEFT JOIN disciplines d ON d.id = g.discipline
                 LEFT JOIN teachers t ON t.id = d.teacher
                 WHERE g.student = ? AND t.id = ?"""
        cur.execute(sql, (id_student, id_teacher))
        print(cur.fetchall())


"""Средний балл, который преподаватель ставит студенту."""


def query_11(id_student: int, id_teacher: int):
    with sqlite3.connect("education.db") as conn:
        cur = conn.cursor()
        sql = """SELECT DISTINCT s.student, t.teacher, round(avg(grade), 2) AS avg_grade
                 FROM grades g
                 LEFT JOIN students s ON s.id = g.student
                 LEFT JOIN disciplines d ON d.id = g.discipline
                 LEFT JOIN teachers t ON t.id = d.teacher
                 WHERE g.student = ? AND t.id = ?
                 GROUP BY s.student, t.teacher"""
        cur.execute(sql, (id_student, id_teacher))
        print(cur.fetchall())


"""Средний балл, который ставит преподаватель."""


def query_12(id_teacher: int):
    with sqlite3.connect("education.db") as conn:
        cur = conn.cursor()
        sql = """SELECT DISTINCT t.teacher, round(avg(grade), 2) AS avg_grade
                 FROM grades g
                 LEFT JOIN disciplines d ON d.id = g.discipline
                 LEFT JOIN teachers t ON t.id = d.teacher
                 WHERE t.id = ?
                 GROUP BY t.teacher"""
        cur.execute(sql, (id_teacher,))
        print(cur.fetchall())


if __name__ == "__main__":
    query_2(2)
    query_3(1)
    query_4()
    query_5(3)
    query_6(2)
    query_7(1, 1)
    query_8(4, 2)
    query_9(12)
    query_10(10, 3)
    query_11(5, 1)
    query_12(3)
