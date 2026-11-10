# DevOps Service Project

A reliable internal service information page developed as part of the DevOps and System Administration course.

## Project Structure
- `app.py`: Main Python web application including the `/health` endpoint and version info.
- `Dockerfile`: Container image build recipe (configured to run without root privileges).
- `requirements.txt`: Project Python dependencies.
- `docs/`: Documentation folder including Linux environment setup (`linux-setup.md`).
- `.github/workflows/ci.yml`: Automated CI pipeline configuration.

## How to Build and Run Locally

1. **Build the Docker Image:**
   ```bash
   docker build -t devops-service:v1.0 .
