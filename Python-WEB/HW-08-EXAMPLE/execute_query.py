import sqlite3

'''Собственно - сама функция))) Принимает на вход текстовый скрипт возвращает список с результатами выполнения. Если в запросе ничего не вернулось - вернёт пусто список'''

def execute_query(sql: str) -> list:
    '''открываем соединение с БД'''
    with sqlite3.connect('salary.db') as con:
        '''Создаём курсор'''
        cur = con.cursor()
        '''Выполняем запрос'''
        cur.execute(sql)
        '''Возвращаем результат'''
        return cur.fetchall()


if __name__ == "__main__":
    query_name = 'query_3.sql'
    with open(query_name, 'r') as f:
        sql = f.read()
        print(execute_query(sql))
