from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.core.ollama_client import ask_ollama
from src.core.db import get_connection
from src.core.utils import map_sql_row_to_result

router = APIRouter()

class SearchInput(BaseModel):
    question: str
    model: str = "gemma3:1b-it-qat"

@router.post("/search")
def search_text_to_sql(payload: SearchInput):
    question = payload.question
    model = payload.model

    # Recupera lo schema dinamico
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SHOW TABLES;")
    schema_lines = []
    for (table,) in cur.fetchall():
        cur.execute(f"SHOW COLUMNS FROM {table}")
        columns = [col[0] for col in cur.fetchall()]
        schema_lines.append(f"Table {table}: columns {', '.join(columns)}")
    cur.close()
    conn.close()

    prompt = f"""
Schema del database:
{chr(10).join(schema_lines)}

Genera una singola query SQL (solo SELECT) per rispondere alla domanda:
{question}
La query deve essere sintatticamente corretta per MariaDB.
"""

    try:
        sql = ask_ollama(model, prompt).strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ollama error: {str(e)}")

    if not sql.lower().startswith("select"):
        return {"sql": sql, "sql_validation": "unsafe", "results": None}

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        columns = [desc[0] for desc in cur.description]
        results = [map_sql_row_to_result(row, columns) for row in rows]
        cur.close()
        conn.close()
        return {"sql": sql, "sql_validation": "valid", "results": results}
    except Exception as e:
        return {"sql": sql, "sql_validation": "invalid", "results": None, "error": str(e)}
