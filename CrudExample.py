from database import DatabaseContextManager


def create_table_customer():
    query = """CREATE TABLE IF NOT EXISTS Customer(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    age INTEGER,
    FOREIGN KEY (company_id) REFERENCES Companies(id))"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def create_customer(first_name: str, last_name: str, age: int):
    query = """INSERT INTO Customer(first_name, last_name, age, company_id) VALUES(?,?,?)"""
    parameters = [first_name, last_name, age]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def get_customer():
    query = """SELECT * FROM Customer"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)


def update_customer_age(old_age: int, new_age: int):
    query = """UPDATE Customer
                SET age = ?
                WHERE age = ?"""
    parameters = [new_age, old_age]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def delete_customer(last_name: str):
    query = """DELETE FROM Customer
                WHERE last_name = ?"""
    parameters = [last_name]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)
