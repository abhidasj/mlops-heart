# -----------------------------
#   Base Image
# -----------------------------
FROM python:3.10-slim

# -----------------------------
#   Working Directory
# -----------------------------
WORKDIR /app

# -----------------------------
#   Install System Dependencies
# -----------------------------
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# -----------------------------
#   Copy Requirements
# -----------------------------
COPY requirements.txt .

# -----------------------------
#   Install Python Dependencies
# -----------------------------
RUN pip install --no-cache-dir -r requirements.txt

# -----------------------------
#   Copy Source Code
# -----------------------------
COPY src/ ./src/
COPY data/ ./data/
COPY models/ ./models/

# -----------------------------
#   Environment Variables
# -----------------------------
ENV PYTHONUNBUFFERED=1

# -----------------------------
#   Run Training Script
# -----------------------------
CMD ["python", "src/train.py"]
