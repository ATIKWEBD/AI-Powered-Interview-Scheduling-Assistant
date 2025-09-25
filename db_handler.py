# db_handler.py
import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_db_connection():
    """Establishes a connection to the MySQL database."""
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error connecting to database: {err}")
        return None

def save_interview(candidate_name: str, schedule_data: dict):
    """Saves a new interview schedule to the database."""
    conn = get_db_connection()
    if not conn:
        return False

    try:
        cursor = conn.cursor()
        sql = """
        INSERT INTO interviews (candidate_name, scheduled_date, start_time, end_time)
        VALUES (%s, %s, %s, %s)
        """
        val = (
            candidate_name,
            schedule_data.get('date'),
            schedule_data.get('start_time'),
            schedule_data.get('end_time')
        )
        cursor.execute(sql, val)
        conn.commit()
        print(f"{cursor.rowcount} record inserted successfully.")
        return True
    except mysql.connector.Error as err:
        print(f"Error inserting record: {err}")
        return False
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()