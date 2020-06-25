import random
import numpy as np
import sqlite3
from sqlite3 import Error

random.seed()


def get_db(db_file):
    """ Create a connection to our SQLite database"""
    conn = None
    conn = sqlite3.connect(db_file)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS card (
            id INTEGER PRIMARY KEY,
            number TEXT NOT NULL UNIQUE,
            pin TEXT NOT NULL,
            balance INTEGER DEFAULT 0
        )
    """)
    conn.commit()

    return conn


def save_account(db, acc, pin):
    sql = """
        INSERT INTO card (number, pin) 
        VALUES ('{}', '{}')
    """.format(acc, pin)

    db.execute(sql)
    db.commit()


def valid_login(db, acc, pin):
    result = db.execute("""
            SELECT pin
            FROM card
            WHERE number = '{}'
        """.format(acc)).fetchone()

    if result:
        return pin == result[0]
    return False


def get_balance(db, acc):
    return db.execute("""
            SELECT balance
            FROM card
            WHERE number = '{}'
        """.format(acc)).fetchone()[0]


def close_account(db, acc):
    sql = """
        DELETE FROM card
        WHERE number = '{}'
    """.format(acc, acc)
    db.execute(sql)
    db.commit()


def add_income(db, acc, amount):
    sql = """
        UPDATE card
        SET balance = {}
        WHERE number = '{}'
    """.format(amount, acc)
    print(sql)
    db.execute(sql)
    db.commit()


def account_exists(db, number):
    result = db.execute("""
                SELECT pin
                FROM card
                WHERE number = '{}'
            """.format(number)).fetchone()
    if result:
        return True
    return False


def create_account():
    iin = 400000
    account_number = random.randint(100000000, 999999999)
    checksum = get_luhn_checksum(iin, account_number)

    card_number = str(iin) + str(account_number) + str(checksum)

    print("Your card number:")
    print(card_number)

    return card_number


def generate_pin():
    pin = "%04d" % random.randint(0000, 9999)

    print("Your card PIN:")
    print(pin)

    return pin


def transfer(db, sender_account):
    print("Transfer")
    print("Enter card number: ")
    receiver_account = input()

    if sender_account == receiver_account:
        print("You can't transfer money to the same account!")
    elif invalid_account(receiver_account):
        print("Probably you made a mistake in the card number. Please try again!")
    elif not account_exists(db, receiver_account):
        print("Such a card does not exist.")
    else:
        print("Enter how much money you want to transfer: ")
        amount = int(input())

        sender_balance = int(get_balance(db, sender_account))

        if amount > sender_balance:
            print("Not enough money!")
        else:
            receiver_balance = int(get_balance(db, receiver_account)) + amount
            add_income(db, receiver_account, receiver_balance)
            add_income(db, sender_account, sender_balance - amount)
            print("Success!")


def get_luhn_checksum(iin, account_number):
    iin_list = [int(x) for x in str(iin)]
    acc_list = [int(x) for x in str(account_number)]
    numbers = iin_list + acc_list

    luhn = []

    for i in range(len(numbers)):
        if i % 2 != 0:
            luhn.append(numbers[i])
        else:
            n = numbers[i] * 2
            luhn.append(n if n <= 9 else n - 9)

    final_sum = np.sum([luhn])

    for x in range(10):
        if (final_sum + x) % 10 == 0:
            return x


def invalid_account(number):
    check = get_luhn_checksum(number[:-1], '')
    return not check == int(number[-1])


def login(db):
    exit = 0
    print("Enter your card number:")
    card = input()

    print("Enter your PIN:")
    pin = input()

    if valid_login(db, card, pin):
        print("You have successfully logged in!")
        exit = account(card)
    else:
        print("Wrong card number or PIN!")
    return exit


def account(card):
    exit = 1
    menu = """
            1. Balance
            2. Add income
            3. Do transfer
            4. Close account
            5. Log out
            0. Exit
            """
    option = input(menu)

    while option != '0' and option != '5':
        # Get balance
        if option == '1':
            print(get_balance(db, card))

        # Add income
        if option == '2':
            deposit = input("Enter income: ")
            amount = int(get_balance(db, card)) + int(deposit)
            print(amount)
            add_income(db, card, amount)
            print("Income was added!")

        # Do transfer
        if option == '3':
            transfer(db, card)

        # Close account
        if option == '4':
            close_account(db, card)

        option = input(menu)

    if option == '5':
        print("You have successfully logged out!")
        exit = 0

    return exit


if __name__ == '__main__':
    database = 'card.s3db'
    db = ""

    try:
        db = get_db(database)

        menu = """
                1. Create an account
                2. Log into account
                0. Exit
                """

        user_option = str(input(menu))

        while user_option != '0':
            print(user_option)
            if user_option == '1':
                card = create_account()
                pin = generate_pin()
                save_account(db, card, pin)

            if user_option == '2':
                exit = login(db)
                if exit == 1:
                    break

            user_option = str(input(menu))

        print("Bye!")

    except Error as e:
        print(e)

    finally:
        if db:
            db.close()
