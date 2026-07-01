import sqlite3

def create_table():

    conn = sqlite3.connect("passwords.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS passwords(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            website TEXT,

            username TEXT,

            password TEXT,

            category TEXT,

            notes TEXT,

            username_owner TEXT
        )
        """
    )

    conn.commit()

    conn.close()

def save_password_db(

    website,
    username,
    password,
    category,
    notes,
    owner

):

    conn = sqlite3.connect("passwords.db")

    cursor = conn.cursor()

    cursor.execute(

        """
        INSERT INTO passwords
        (
            website,
            username,
            password,
            category,
            notes,
            username_owner
        )

        VALUES (?, ?, ?, ?, ?, ?)
        """,

        (
            website,
            username,
            password,
            category,
            notes,
            owner
        )

    )

    conn.commit()

    conn.close()

def view_passwords_db(owner):

    conn = sqlite3.connect("passwords.db")

    cursor = conn.cursor()

    cursor.execute(

        """
        SELECT *
        FROM passwords
        WHERE username_owner=?
        """,

        (
            owner,
        )

    )

    data = cursor.fetchall()

    conn.close()

    return data

def search_password_db(

    website,
    owner

):

    conn = sqlite3.connect("passwords.db")

    cursor = conn.cursor()

    cursor.execute(

        """
        SELECT *
        FROM passwords
        WHERE website LIKE ?
        AND username_owner=?
        """,

        (
            "%" + website + "%",
            owner
        )

    )

    data = cursor.fetchall()

    conn.close()

    return data

def delete_password_db(

    website,
    owner

):

    conn = sqlite3.connect("passwords.db")

    cursor = conn.cursor()

    cursor.execute(

        """
        DELETE FROM passwords
        WHERE website=?
        AND username_owner=?
        """,

        (
            website,
            owner
        )

    )

    conn.commit()

    conn.close()
