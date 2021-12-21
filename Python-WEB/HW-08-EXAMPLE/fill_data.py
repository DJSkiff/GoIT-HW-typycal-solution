from datetime import datetime
import faker
from random import randint, choice
import sqlite3


def fill_data():
    
    '''Создадим объект класса faker, в качестве параметра передаем локаль для генерации результатов'''
    
    fake_data = faker.Faker('uk-UA')

    '''Создадим структуры для наполнения их данными'''
    
    companies = [] # здесь будем хранить компании
    employees = [] # здесь будем хранить сотрудников
    posts = [] # здесь будем хранить должности

    '''Возьмём три компании из faker и поместим их в нужную переменную'''
    
    for _ in range(3):
        companies.append(fake_data.company())

    '''Теперь создадим 30 сотрудников'''
    
    for _ in range(30):
        employees.append(fake_data.name())

    '''И 5 должностей'''
    
    for _ in range(5):
        posts.append(fake_data.job())

    '''Так как для выполнения скрипта на множественную вставку данных в таблицу нам потребуется список списков - создадим такой для каждой из таблиц '''
    
    for_employees = [] # для таблицы employees

    for emp in employees:
        
        '''Перебираем всех сотрудников, и к каждому добавляем должность и id компании. Компаний у нас 3, при создании таблицы companies для поля id мы указыли INTEGER AUTOINCREMENT - потому каждая запись будет получать последовательное число увеличенное на 1, начиная с 1. Потому компанию выбираем рандомно)))'''
        
        for_employees.append([emp, choice(posts), randint(1, 3)])

    '''Тоже выполним и для таблицы выплаты зарплат. по умолчанию зададим, что выплата зарплаты во всех компаниях выполнялась 7 числа каждого месяца. Вилку зарплат згенерим в диапазоне от 1000 до 10000 у.е. Генерить будем для каждого месяца, и каждого сотрудника. '''
    
    for_payments = []

    for month in range(1, 12+1):
        
        '''Здесь происходит цикл по месяцам'''
        
        payment_date = datetime(2021, month, 7).date()
        
        for emp in range(1, 30+1):
            
            '''Здесь - по id сотрудников'''
            
            for_payments.append([emp, payment_date, randint(1000, 10000)])

    '''Все данные у нас есть можно их заганять в таблицы.
    Первым делом создадим соединение с нашей БД и получим объект курсора для манипуляций с данными'''
    
    with sqlite3.connect('salary.db') as con:
        
        cur = con.cursor()

        '''Первым делом вставляем компании. Напишем для него скрипт, а переменные, которые будем вставлять заполним заполнителем (?)'''
        
        sql_to_companies = """INSERT INTO companies(company_name)
                              VALUES (?)"""
        
        '''Для вставки сразу всех данных воспользуемся методом executemany курсора. Первым параметром будет скрипт, а вторым данные (список списков). Так как кроме названия компаний у нас ничего нет, применим к списку с именами компаний функцию zip, и получим, то что нам нужно)'''
        
        cur.executemany(sql_to_companies, zip(companies,))

        '''Далее вставляем данные о сотрудниках. Напишем для него скрипт. И укажем переменные'''
        
        sql_to_employees = """INSERT INTO employees(employee, post, company)
                              VALUES (?, ?, ?)"""
                              
        '''Данные были подготовлены заранее, потому просто передаем их в функцию'''
        
        cur.executemany(sql_to_employees, for_employees)

        '''аналогично предыдущим двум действиям'''
        
        sql_to_payments = """INSERT INTO payments(employee, date_of, total)
                             VALUES (?, ?, ?)"""
                             
        '''легко и просто вставляем данные о зарплатах)'''
        
        cur.executemany(sql_to_payments, for_payments)

        '''Не забываем фиксировать наши изменения в БД'''
        
        con.commit()


if __name__ == "__main__":
    fill_data()