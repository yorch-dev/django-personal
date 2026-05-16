FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

ARG UID=1000
ARG GID=1000

RUN mkdir -p /app/.cache/uv /app/productionstaticfiles \
    && chown -R ${UID}:${GID} /app/.cache/uv /app/productionstaticfiles

ENV UV_CACHE_DIR=/app/.cache/uv

RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir uv

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

ENV PATH="/app/.venv/bin:$PATH"

COPY . .

EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
