from fastapi import APIRouter
from src.core.db import get_connection

router = APIRouter()

@router.get("/schema_summary")
def schema_summary():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SHOW TABLES;")
    tables = [row[0] for row in cur.fetchall()]

    schema = []
    for table in tables:
        cur.execute(f"SHOW COLUMNS FROM {table}")
        columns = cur.fetchall()
        for col in columns:
            schema.append({
                "table_name": table,
                "table_column": col[0]
            })

    cur.close()
    conn.close()

    return schema