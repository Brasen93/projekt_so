import sqlite3
import random

conn = sqlite3.connect('bank_db.db')
c = conn.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS bank_clients(pesel INTEGER, first_name TEXT, last_name TEXT, account_no INTEGER, balance REAL)')


def data_entry():
    c.execute("INSERT INTO bank_clients VALUES(1234, 'Jan', 'Kowalski', 123456)")
    conn.commit()
    c.close()
    conn.close()


def dynamic_data_entry(pesel, first_name, last_name):
    account_no = random.randrange(1000, 9999)
    balance = 0
    c.execute("INSERT INTO bank_clients (pesel, first_name, last_name, account_no, balance) VALUES (?, ?, ?, ?, ?)",
              (pesel, first_name, last_name, account_no, balance))
    conn.commit()


def account_exists(account_no):
    c.execute("SELECT * FROM bank_clients WHERE account_no=?", (account_no,))
    for row in c.fetchall():
        return row[0]


def display_balance(account_no):
    c.execute("SELECT balance FROM bank_clients WHERE account_no=?", (account_no,))
    for row in c.fetchall():
        return row[0]


def update_balance(account_no, new_balance):
    c.execute('UPDATE bank_clients SET balance = ? WHERE account_no=?', (new_balance, account_no,))
    conn.commit()


c.close()
conn.close()
