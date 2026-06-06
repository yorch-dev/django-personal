FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="${VIRTUAL_ENV}/bin:$PATH"
ENV UV_CACHE_DIR=/app/.cache/uv
ENV HOME=/tmp

WORKDIR /app

ARG UID=1000
ARG GID=1000

RUN mkdir -p /app/.cache/uv /app/productionstaticfiles \
    && chown -R ${UID}:${GID} /app/.cache/uv /app/productionstaticfiles

RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir uv

COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev \
    && chown -R ${UID}:${GID} /app/.venv /app/.cache/uv /app/productionstaticfiles

COPY . .

EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
