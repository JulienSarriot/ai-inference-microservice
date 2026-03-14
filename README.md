# AI Inference Microservice

A production-ready microservice for asynchronous AI model inference. Built with **FastAPI**, **Celery**, and **Redis**.

## Architecture

The system uses an asynchronous task queue to handle long-running AI inference tasks without blocking the web server.

`mermaid
graph LR
    User[Client] -- POST /inference --> API[FastAPI]
    API -- Push Task --> Redis[(Redis Broker)]
    Redis -- Pull Task --> Worker[Celery Worker]
    Worker -- Execute Model --> Model((AI Model))
    Model -- Return Result --> Worker
    Worker -- Store Result --> Redis
    API -- Polling Result --> Redis
    API -- Job Status --> User
`

## Features

- **Asynchronous Processing**: Offload heavy computations to background workers.
- **Scalable**: Easily scale workers independently of the API.
- **Modern Stack**: FastAPI for high-performance API, Pydantic for data validation.
- **Containerized**: Fully Dockerized for consistent development and deployment.

## Getting Started

### Prerequisites

- Docker and Docker Compose

### Installation & Run

1. **Clone the repository**:
   `ash
   git clone https://github.com/JulienSarriot/ai-inference-microservice.git
   cd ai-inference-microservice
   `

2. **Start the services**:
   `ash
   docker-compose up --build
   `

3. **Access the API**:
   - API: http://localhost:8000
   - Documentation (Swagger): http://localhost:8000/docs

## API Endpoints

### 1. Submit Inference Job
- **URL**: /inference
- **Method**: POST
- **Payload**:
  `json
  {
    "model_id": "resnet-50",
    "input_data": {"image_url": "https://example.com/image.jpg"}
  }
  `
- **Response**: 202 Accepted with job_id.

### 2. Check Job Status
- **URL**: /status/{job_id}
- **Method**: GET
- **Response**: Current status (PENDING, SUCCESS, etc.) and result if available.

## Project Structure

`	ext
.
├── app/
│   ├── core/
│   │   └── config.py    # Configuration management
│   ├── main.py          # FastAPI application
│   ├── schemas.py       # Pydantic models
│   ├── tasks.py         # Celery tasks
│   └── worker.py        # Celery application
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
`

## License
MIT