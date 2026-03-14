from fastapi import FastAPI, HTTPException, status
from app.schemas import InferenceRequest, JobStatus
from app.tasks import run_inference
from celery.result import AsyncResult

app = FastAPI(
    title="AI Inference Microservice",
    description="Scalable AI model inference using FastAPI, Celery, and Redis.",
    version="1.0.0"
)

@app.post(
    "/inference",
    response_model=JobStatus,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Submit an inference job"
)
async def submit_inference(request: InferenceRequest):
    """
    Submits a new inference job to the worker queue.
    """
    task = run_inference.delay(request.model_id, request.input_data)
    return JobStatus(job_id=task.id, status="PENDING")

@app.get(
    "/status/{job_id}",
    response_model=JobStatus,
    summary="Check job status"
)
async def get_status(job_id: str):
    """
    Retrieves the status and result (if completed) of an inference job.
    """
    res = AsyncResult(job_id)
    
    if res.failed():
        return JobStatus(job_id=job_id, status="FAILURE", result={"error": str(res.result)})
        
    if res.ready():
        return JobStatus(job_id=job_id, status="SUCCESS", result=res.result)
        
    return JobStatus(job_id=job_id, status=res.status)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}