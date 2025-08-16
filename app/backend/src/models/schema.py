from pydantic import BaseModel

class AddLine(BaseModel):
    data_line: str

class QuestionInput(BaseModel):
    question: str
    
class SqlQueryInput(BaseModel):
    sql_query: str
