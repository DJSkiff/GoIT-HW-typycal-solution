from datetime import datetime
import faker
from random import randint, choice
import sqlite3


def fill_data():

    fake_data = faker.Faker('uk-UA')

    companies = []
    employees = []
    posts = []

    for _ in range(3):
        companies.append(fake_data.company())

    for _ in range(30):
        employees.append(fake_data.name())

    for _ in range(5):
        posts.append(fake_data.job())

    for_employees = []

    for emp in employees:
        for_employees.append([emp, choice(posts), randint(1, 3)])

    for_payments = []

    for month in range(1, 12+1):
        payment_date = datetime(2021, month, 7).date()
        for emp in range(1, 30+1):
            for_payments.append([emp, payment_date, randint(1000, 10000)])

    with sqlite3.connect('salary.db') as con:
        cur = con.cursor()

        sql_to_companies = """INSERT INTO companies(company_name)
                              VALUES (?)"""
        cur.executemany(sql_to_companies, zip(companies,))

        sql_to_employees = """INSERT INTO employees(employee, post, company)
                              VALUES (?, ?, ?)"""
        cur.executemany(sql_to_employees, for_employees)

        sql_to_payments = """INSERT INTO payments(employee, date_of, total)
                             VALUES (?, ?, ?)"""
        cur.executemany(sql_to_payments, for_payments)

        con.commit()


if __name__ == "__main__":
    fill_data()