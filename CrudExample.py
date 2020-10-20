from database import DatabaseContextManager


def create_table_customer():
    query = """CREATE TABLE IF NOT EXISTS Customer(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
    last_name TEXT,
    age INTEGER,
    company_id INTEGER,
    FOREIGN KEY (company_id) REFERENCES Companies(id))"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def create_customer(first_name: str, last_name: str, age: int, company_id: int):
    query = """INSERT INTO Customer(first_name, last_name, age, company_id) VALUES(?,?,?,?)"""
    parameters = [first_name, last_name, age, company_id]
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


def create_table_companies():
    query = """CREATE TABLE IF NOT EXISTS Companies(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT,
    employee_count INTEGER,
    average_salary FLOAT)"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def create_campanies(company_name: str, employee_count: int, average_salary: float):
    query = """INSERT INTO Companies(company_name, employee_count, average_salary) VALUES(?,?,?)"""
    parameters = [company_name, employee_count, average_salary]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def get_customer_companies():
    query = """SELECT * FROM Customer
            JOIN Companies
                ON company_id = Companies.id"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)


def drop_table():
    query = """DROP TABLE Customer"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


get_customer_companies()
