import sqlite


def check_if_account_exists(account_no):
    if not sqlite.account_exists(account_no):
        return False


def withdraw_money(account_no, amount):
    current_balance = int(sqlite.display_balance(account_no))
    balance_after_withdraw = current_balance - int(amount)
    if balance_after_withdraw < 0:
        return False
    sqlite.update_balance(account_no, balance_after_withdraw)
    return balance_after_withdraw


def deposit_money(account_no, amount):
    current_balance = int(sqlite.display_balance(account_no))
    balance_after_deposit = current_balance + int(amount)
    return balance_after_deposit


