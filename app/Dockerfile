# Use an official Python runtime as a parent image
FROM python:3.12-alpine

# Create a non-root user
RUN adduser -D fastapiuser

#Install uv for fast package installation
RUN pip install uv
# Install all required packages 
RUN uv pip install --no-cache-dir --system fastapi uvicorn gunicorn

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 80 available to the world outside this container
EXPOSE 80

# Switch to the fastapi user
USER fastapiuser

# Run app.py when the container launches
CMD ["gunicorn", "-c", "gunicorn-config.py", "app:app"]
