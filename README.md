# Jupyter Server Docker Container

This repository contains a Dockerfile configured to run a Jupyter Server with NVIDIA CUDA support, enabling GPU usage through Docker containers.

<div style="display: flex; justify-content: center; align-items: center; gap: 20px;">
  <div style="text-align: center;">
    <img src="https://docscontent.nvidia.com/dims4/default/f916ffc/2147483647/strip/true/crop/1020x969+0+0/resize/1020x969!/format/webp/quality/90/?url=https%3A%2F%2Fk3-prod-nvidia-docs.s3.us-west-2.amazonaws.com%2Fbrightspot%2Fdita%2F00000195-450d-d2f7-a3df-df4f21df0000%2Fdeeplearning%2Fframeworks%2Fuser-guide%2Fgraphics%2Fsoftware_stack_zoom.png" alt="NVIDIA Docker Containers" width="300">
    <br>
    <strong>NVIDIA Docker Containers</strong>
  </div>
  <div style="text-align: center;">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Jupyter_logo.svg/1200px-Jupyter_logo.svg.png" alt="Jupyter Server" width="300">
    <br>
    <strong>Jupyter Server</strong>
  </div>
</div>

## Features

- **NVIDIA CUDA Support:** Run the Jupyter server using the GPU via Docker.
- **Data Persistence:**
  - Jupyter working directory: `/app/jupyter_workspace`
  - Virtual environment with installed packages (pip): `/app/venv`

## How to Get Started

### 1. Build the Docker Image

Build the image by running the following command:

```bash
docker build -t erikyvanov-jupyter-server .
```

### 2. Initialize Virtual Environment Persistence (Run only once)
Copy the original virtual environment from the image to initialize venv persistence:

```bash
mkdir -p $(pwd)/jupyter_server
docker create --name erikyvanov-jupyter-server_temp_copy erikyvanov-jupyter-server
docker cp erikyvanov-jupyter-server_temp_copy:/app/venv $(pwd)/jupyter_server
docker rm erikyvanov-jupyter-server_temp_copy
```

### 3. Run the Jupyter Server
Start the container and run the Jupyter server with the following command:

```bash
docker run --gpus all \
  -p 8888:8888 \
  -v $(pwd)/jupyter_server/jupyter_workspace:/app/jupyter_workspace \
  -v $(pwd)/jupyter_server/venv:/app/venv \
  erikyvanov-jupyter-server
```

Once started, access your Jupyter server at `http://localhost:8888`