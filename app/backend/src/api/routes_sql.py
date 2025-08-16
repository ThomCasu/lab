from fastapi import APIRouter
from pydantic import BaseModel
from src.core.db import get_connection
from src.core.utils import map_sql_row_to_result

router = APIRouter()

class SQLSearchInput(BaseModel):
    sql_query: str

@router.post("/sql_search")
def sql_search(payload: SQLSearchInput):
    sql_query = payload.sql_query.strip()

    if not sql_query.lower().startswith("select"):
        return {"sql_validation": "unsafe", "results": None}

    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(sql_query)
        rows = cur.fetchall()
        columns = [desc[0] for desc in cur.description]
        results = [map_sql_row_to_result(row, columns) for row in rows]
        cur.close()
        conn.close()
        return {"sql_validation": "valid", "results": results}
    except Exception as e:
        return {"sql_validation": "invalid", "results": None, "error": str(e)}
