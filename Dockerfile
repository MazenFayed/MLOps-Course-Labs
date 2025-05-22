# Use official Python base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy all files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port FastAPI will run on
EXPOSE 8000

# Command to run the FastAPI app
CMD ["uvicorn", "src.MLOps_Course_Labs.main:app", "--host", "0.0.0.0", "--port", "8000"]
