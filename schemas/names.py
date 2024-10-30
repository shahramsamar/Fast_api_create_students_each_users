from pydantic import BaseModel

class NamesSchema(BaseModel):
    name : str 
    
class ResponseNamesSchema(NamesSchema):
    id: int
