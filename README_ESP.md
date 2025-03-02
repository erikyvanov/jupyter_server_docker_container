# Jupyter Server Docker Container

Este repositorio contiene un Dockerfile configurado para ejecutar un servidor de Jupyter con soporte para NVIDIA CUDA, permitiendo utilizar la GPU a través de contenedores Docker.


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


## Características

- **Soporte para NVIDIA CUDA:** Ejecuta el servidor Jupyter utilizando la GPU a través de Docker.
- **Persistencia de Datos:**
  - Directorio de trabajo de Jupyter: `/app/jupyter_workspace`
  - Entorno virtual con los paquetes instalados (pip): `/app/venv`

## Cómo Empezar

### 1. Compilación de la Imagen Docker

Construye la imagen ejecutando el siguiente comando:

```bash
docker build -t erikyvanov-jupyter-server .
```
### 2. Inicialización de la Persistencia del Entorno Virtual (Solo se realiza una vez)
Copia el entorno virtual original de la imagen para inicializar la persistencia del venv:
```bash
mkdir -p $(pwd)/jupyter_server
docker create --name erikyvanov-jupyter-server_temp_copy erikyvanov-jupyter-server
docker cp erikyvanov-jupyter-server_temp_copy:/app/venv $(pwd)/jupyter_server
docker rm erikyvanov-jupyter-server_temp_copy
```

### 3. Ejecución del Servidor de Jupyter
Inicia el contenedor y ejecuta el servidor de Jupyter con el siguiente comando:
```bash
docker run --gpus all \
  -p 8888:8888 \
  -v $(pwd)/jupyter_server/jupyter_workspace:/app/jupyter_workspace \
  -v $(pwd)/jupyter_server/venv:/app/venv \
  erikyvanov-jupyter-server
```

Una vez iniciado, accede a tu servidor Jupyter a través de `http://localhost:8888`
