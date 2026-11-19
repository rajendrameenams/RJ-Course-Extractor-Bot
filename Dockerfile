# Use official lightweight Python 3.11 image (Required for Pyrogram / Kurigram & Pyromod stability)
FROM python:3.11-slim

# Avoid writing .pyc files & force unbuffered stdout/stderr (crucial for real-time Docker/Coolify logs)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=8080

# Set working directory inside container
WORKDIR /app

# Install system dependencies (ffmpeg for video handling, curl for health checks, build essentials)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    libffi-dev \
    ffmpeg \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Copy and install python dependencies first (cached across builds)
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy all project files into the container
COPY . .

# Expose the web server port for Coolify / Render / Railway health checks
EXPOSE 8080

# Container healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=15s --retries=3 \
    CMD curl -f http://127.0.0.1:${PORT:-8080}/ || exit 1

# Start the bot
CMD ["python", "main.py"]
