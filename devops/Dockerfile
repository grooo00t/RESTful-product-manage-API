FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    curl \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Install poetry
RUN pip install poetry

# Copy project files first
COPY . .

# Install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Make entrypoint executable
RUN chmod +x /app/scripts/entrypoint.sh && \
    sed -i 's/\r$//' /app/scripts/entrypoint.sh

ENTRYPOINT ["sh", "/app/scripts/entrypoint.sh"] 