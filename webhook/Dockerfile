FROM python:3.10-slim

# Install curl, bash, and Helm
RUN apt-get update && \
    apt-get install -y curl bash && \
    curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

# Create app directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose Flask port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
