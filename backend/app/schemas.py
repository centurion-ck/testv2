from pydantic import BaseModel

class ThreatRequest(BaseModel):

    process_name: str
    cpu_usage: float
    memory_usage: float

class ThreatResponse(BaseModel):

    prediction: str
    score: float