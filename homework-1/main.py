"""Скрипт для заполнения данными таблиц в БД Postgres."""
"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

with open('./north_data/customers_data.csv') as file:
    customers_data = []
    data_csv = csv.reader(file, delimiter=",")
    for line in data_csv:
        info_csc = tuple(line)
        customers_data.append(info_csc)

with open('./north_data/employees_data.csv') as file:
    employees_data = []
    data_csv = csv.reader(file, delimiter=",")
    for line in data_csv:
        info_csc = tuple(line)
        employees_data.append(info_csc)

with open('./north_data/orders_data.csv') as file:
    orders_data = []
    data_csv = csv.reader(file, delimiter=",")
    for line in data_csv:
        info_csc = tuple(line)
        orders_data.append(info_csc)


conn = psycopg2.connect(host='localhost', database='north',
                        user='postgres', password='123406@aLINA')

cur = conn.cursor()

cur.executemany('INSERT INTO customers VALUES (%s, %s, %s)', customers_data)
cur.executemany('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)', employees_data)
cur.executemany('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', orders_data)
conn.commit()

cur.close()
conn.close()

