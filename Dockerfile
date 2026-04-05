FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN pip install uv

WORKDIR /app

# Copy dependency files first (layer caching)
COPY pyproject.toml uv.lock ./

# Copy source code
COPY src/ src/

# Install dependencies from lock file
RUN uv sync --frozen --no-dev

# Ensure the static directory exists for generated mockup images
RUN mkdir -p src/mobile_app_shipping/static

# HF Spaces requires port 7860
ENV PORT=7860
# Skip auto-opening the browser
ENV ENV=production
# Unbuffered output so logs appear in real time
ENV PYTHONUNBUFFERED=1

EXPOSE 7860

CMD ["uv", "run", "kickoff"]
