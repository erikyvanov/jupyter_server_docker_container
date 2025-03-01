FROM nvidia/cuda:12.8.0-cudnn-devel-ubuntu22.04


ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    software-properties-common \
    wget \
    gnupg \
    libvpx-dev \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

RUN add-apt-repository ppa:deadsnakes/ppa

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.11 \
    python3.11-venv \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN python3.11 -m venv /app/venv

RUN /app/venv/bin/pip install --no-cache-dir --upgrade pip

RUN /app/venv/bin/pip install --no-cache-dir jupyter-server

RUN /app/venv/bin/pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126

RUN /app/venv/bin/pip install --no-cache-dir opencv-python

COPY jupyter_server_config.py /app/jupyter_workspace/jupyter_server_config.py

VOLUME /app/jupyter_workspace
VOLUME /app/venv

WORKDIR /app/jupyter_workspace

EXPOSE 8888

CMD ["/bin/bash", "-c", ". /app/venv/bin/activate && jupyter server --notebook-dir=/app/jupyter_workspace --ip=0.0.0.0 --port=8888 --allow-root"]
