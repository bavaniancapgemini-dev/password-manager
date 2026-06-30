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
            website,
            username,
            password,
            category,
            notes,
            created_at
        )

        VALUES (?, ?, ?, ?, ?, ?)
        """,

        (
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


def view_passwords_db():

    conn = sqlite3.connect(
        "passwords.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM passwords"
    )

    data = cursor.fetchall()

    conn.close()

    return data


def search_password_db(website):

    conn = sqlite3.connect(
        "passwords.db"
    )

    cursor = conn.cursor()

    cursor.execute(

        """
        SELECT *
        FROM passwords
        WHERE website LIKE ?
        """,

        (
            "%" + website + "%",
        )

    )

    data = cursor.fetchall()

    conn.close()

    return data


def delete_password_db(website):

    conn = sqlite3.connect(
        "passwords.db"
    )

    cursor = conn.cursor()

    cursor.execute(

        """
        DELETE FROM passwords
        WHERE website=?
        """,

        (
            website,
        )

    )

    conn.commit()

    conn.close()


def total_passwords_db():

    conn = sqlite3.connect(
        "passwords.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM passwords"
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total