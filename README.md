#  CardioVision: Cloud-Native Myocardial Strain API

> An end-to-end microservice for automated echocardiogram analysis and myocardial strain tracking (Speckle Tracking) using computer vision.

##  Project Overview
This project is built to automate the analysis of medical video data. The system ingests echocardiogram files, asynchronously processes them using a PyTorch-based machine learning model, and returns key cardiological metrics (e.g., Global Longitudinal Strain).

It is designed with a strong focus on cloud infrastructure (GCP), scalability, and a clean, maintainable microservice architecture.

##  Technology Stack
* **Backend & API:** Python 3.10+, FastAPI, Uvicorn
* **Machine Learning:** PyTorch, OpenCV
* **Infrastructure (Planned):** Docker, Google Cloud Platform (Cloud Run, Cloud Storage, Pub/Sub)
* **Data Processing:** Asynchronous inference pipelines

## System Architecture
*(A detailed system design diagram will be added here)*

![System Architecture](docs/architecture.png)

**Data Flow:**
1. **Client** sends a video file via REST API.
2. **FastAPI Gateway** validates the payload and temporarily stores the data.
3. **ML Engine** performs inference on the video frames to track myocardial speckles.
4. The system calculates the strain metrics and returns a structured `JSON` response.

## 🚀 Getting Started (Local Development)

### Prerequisites
* Python 3.10+
* Git
