import mysql.connector
from config import DB_CONFIG

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

def save_chat(user_message, bot_reply):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = "INSERT INTO chatlogs (user_message, bot_reply) VALUES (%s, %s)"
        cursor.execute(query, (user_message, bot_reply))

        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        print("Database Error:", e)
