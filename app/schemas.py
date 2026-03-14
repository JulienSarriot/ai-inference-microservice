from pydantic import BaseModel
from typing import Optional, Any

class InferenceRequest(BaseModel):
    model_id: str
    input_data: Any

class JobStatus(BaseModel):
    job_id: str
    status: str
    result: Optional[Any] = None