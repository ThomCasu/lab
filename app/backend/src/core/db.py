import mariadb
import os

def get_connection():
    return mariadb.connect(
        host=os.getenv("DB_HOST", "mariadb"),
        port=int(os.getenv("DB_PORT", 3306)),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "rootpassword"),
        database=os.getenv("DB_NAME", "esonero_db")
    )
