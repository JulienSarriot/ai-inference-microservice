import time
import random
from typing import Any
from app.worker import celery_app

@celery_app.task(name="app.tasks.run_inference")
def run_inference(model_id: str, input_data: Any):
    # Simulating heavy computation
    time.sleep(random.randint(2, 5))
    
    return {
        "model_id": model_id,
        "processed_input": input_data,
        "prediction": "Mock prediction result",
        "confidence": round(random.uniform(0.85, 0.99), 4)
    }