import sqlite3

'''Собственно - сама функция))) Принимает на вход текстовый скрипт возвращает список с результатами выполнения. Если в запросе ничего не вернулось - вернёт пусто список'''

def execute_query(sql: str) -> list:
    '''открываем соединение с БД'''
    with sqlite3.connect('education.db') as con:
        '''Создаём курсор'''
        cur = con.cursor()
        '''Выполняем запрос'''
        cur.execute(sql, [2,])
        '''Возвращаем результат'''
        return cur.fetchall()


if __name__ == "__main__":
    # for i in range(1, 12+1):
    #     query_name = f'query_{i}.sql'
    with open('query_2.sql', 'r') as f:
        sql = f.read()
        print(execute_query(sql))
