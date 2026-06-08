import os
import psycopg2
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

DB_HOST     = os.getenv("DB_HOST")
DB_PORT     = os.getenv("DB_PORT")
DB_NAME     = os.getenv("DB_NAME")
DB_USER     = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
 
def get_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        sslmode="require"
    )

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
      CREATE TABLE IF NOT EXISTS water_intake(
      id SERIAL PRIMARY KEY,
      user_id TEXT,
      intake_ml INTEGER,
      date TEXT
    )
    """)
    conn.commit()
    conn.close()

def log_intake(user_id, intake_ml):
    conn = get_connection()
    cursor = conn.cursor()
    date_today = datetime.today().strftime('%Y-%m-%d')
    cursor.execute("INSERT INTO water_intake (user_id, intake_ml, date) VALUES(%s,%s,%s)", (user_id, intake_ml, date_today))
    conn.commit()
    conn.close()

def get_intake_history(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT intake_ml, date FROM water_intake WHERE user_id = %s", (user_id,))
    records = cursor.fetchall()
    conn.close()
    return records

if __name__ == "__main__":
        print("Connecting to:", os.getenv('DB_HOST'), os.getenv('DB_NAME'))
        create_tables()
        print("Tables created successfully!")