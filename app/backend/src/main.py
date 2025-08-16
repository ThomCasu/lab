from src.api.routes_add import router as add_router
from src.api.routes_schema import router as schema_router
from src.api.routes_search import router as search_router
from src.api.routes_sql import router as sql_router
from src.core.db import get_connection
from fastapi import FastAPI

app = FastAPI()

app.include_router(add_router)
app.include_router(schema_router)
app.include_router(search_router)
app.include_router(sql_router)
