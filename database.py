import sqlite3


def create_table():

    conn = sqlite3.connect(
        "passwords.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS passwords(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        username_owner TEXT,

        website TEXT,

        username TEXT,

        password TEXT,

        category TEXT,

        notes TEXT,

        created_at TEXT

        )
        """
    )

    conn.commit()

    conn.close()


def save_password_db(

    username_owner,
    website,
    username,
    password,
    category,
    notes,
    created_at

):

    conn = sqlite3.connect(
        "passwords.db"
    )

    cursor = conn.cursor()

    cursor.execute(

        """
        INSERT INTO passwords
        (
            username_owner,
            website,
            username,
            password,
            category,
            notes,
            created_at
        )

        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,

        (
            username_owner,
            website,
            username,
            password,
            category,
            notes,
            created_at
        )

    )

    conn.commit()

    conn.close()


def view_passwords_db(owner):

    conn = sqlite3.connect(
        "passwords.db"
    )

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


def search_password_db(owner, website):

    conn = sqlite3.connect(
        "passwords.db"
    )

    cursor = conn.cursor()

    cursor.execute(

        """
        SELECT *
        FROM passwords
        WHERE username_owner=? AND website LIKE ?
        """,

        (
            owner,
            "%" + website + "%"
        )

    )

    data = cursor.fetchall()

    conn.close()

    return data


def search_category_db(owner, category):

    conn = sqlite3.connect(
        "passwords.db"
    )

    cursor = conn.cursor()

    cursor.execute(

        """
        SELECT *
        FROM passwords
        WHERE username_owner=? AND category LIKE ?
        """,

        (
            owner,
            "%" + category + "%"
        )

    )

    data = cursor.fetchall()

    conn.close()

    return data


def delete_password_db(owner, website):

    conn = sqlite3.connect(
        "passwords.db"
    )

    cursor = conn.cursor()

    cursor.execute(

        """
        DELETE FROM passwords
        WHERE username_owner=? AND website=?
        """,

        (
            owner,
            website
        )

    )

    conn.commit()

    conn.close()


def total_passwords_db(owner):

    conn = sqlite3.connect(
        "passwords.db"
    )

    cursor = conn.cursor()

    cursor.execute(

        """
        SELECT COUNT(*)
        FROM passwords
        WHERE username_owner=?
        """,

        (
            owner,
        )

    )

    total = cursor.fetchone()[0]

    conn.close()

    return total