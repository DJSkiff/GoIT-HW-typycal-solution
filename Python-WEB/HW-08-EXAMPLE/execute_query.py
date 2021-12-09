import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('salary.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


if __name__ == "__main__":
    query_name = 'query_3.sql'
    with open(query_name, 'r') as f:
        sql = f.read()
        print(execute_query(sql))
