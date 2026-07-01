import sqlite3

def create_user_table():

    conn = sqlite3.connect(
        "users.db"
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT UNIQUE,

            password TEXT
        )
        """
    )

    conn.commit()

    conn.close()

def register_user(

    username,
    password

):

    conn = sqlite3.connect(
        "users.db"
    )

    cursor = conn.cursor()

    try:

        cursor.execute(

            """
            INSERT INTO users
            (
                username,
                password
            )

            VALUES (?, ?)
            """,

            (
                username,
                password
            )

        )

        conn.commit()

        conn.close()

        return True

    except:

        conn.close()

        return False

def login_user(

    username,
    password

):

    conn = sqlite3.connect(
        "users.db"
    )

    cursor = conn.cursor()

    cursor.execute(

        """
        SELECT *
        FROM users
        WHERE username=?
        AND password=?
        """,

        (
            username,
            password
        )

    )

    data = cursor.fetchone()

    conn.close()

    return data
