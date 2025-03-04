# fastapi-docker

Example of a FastApi project using `uv` and deployed in a docker container.

## run local (without docker)

```bash
python main.py
```

## Docker setup

### Dockerfile

Place this file in project root:

```dockerfile
FROM python:3.13-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:0.6.3 /uv /uvx /bin/
ADD . /app
WORKDIR /app
RUN uv sync --frozen
CMD ["uv", "run", "main.py"]
```

### build image

```bash
sudo docker build -t fastapi-docker .
```

check image was created:
```bash
sudo docker images
```
outupt:

```console
REPOSITORY    TAG       IMAGE ID       CREATED          SIZE
fastapi-docker   latest    724f22b7d04a   10 minutes ago   175MB
```

### docker run

Start the container on port 8000

```bash
sudo docker run -it --rm --publish 8000:8000 fastapi-docker
```

### test

in terminal make a http request:

```bash
# PUT request
http PUT 127.0.0.1:8000
# GET request
http GET 127.0.0.1:8000
```

output: 

```console
HTTP/1.1 200 OK
content-length: 219
content-type: application/json
date: Thu, 27 Feb 2025 21:40:36 GMT
server: uvicorn

{
    "body": "",
    "headers": {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "connection": "keep-alive",
        "content-length": "0",
        "host": "127.0.0.1:8000",
        "user-agent": "HTTPie/3.2.2"
    },
    "message": "request received",
    "method": "PUT"
}
```

## Docker compose

- create the file `compose.yml`

```yaml
services:
  web:
    build: .
    ports:
      - "8000:8000"
    develop:
      watch:
        - action: sync
          path: .
          target: /app
          ignore:
            - .venv/
        - action: rebuild
          path: ./uv.lock
```

Start the `run.sh` script, which will call: `docker run` with mount option. Be sure to set execution permission `chmod +x run.sh`.

```bash
sudo ./run.sh
```

check if the container is running:

```bash
sudo docker ps
```
