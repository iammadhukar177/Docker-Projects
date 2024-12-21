# Simple Flask App in Docker

This is a simple Flask application running in a Docker container. It displays "Hello, World!" when accessed.

## Requirements
- Docker
- Python (if building the Docker image locally)

## How to Run
1. Build the Docker image:
    ```bash
    docker build -t simple-flask-app .
    ```

2. Run the Docker container:
    ```bash
    docker run -p 5000:5000 simple-flask-app
    ```

3. Access the app at `http://localhost:5000`.
