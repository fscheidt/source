FROM python:3.13-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:0.6.3 /uv /uvx /bin/
ADD . /app
WORKDIR /app
RUN uv sync --frozen
CMD ["uv", "run", "main.py"]
