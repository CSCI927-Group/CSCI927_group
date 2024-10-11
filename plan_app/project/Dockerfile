# Linux
sudo apt update
sudo apt install docker.io
sudo systemctl start docker
sudo systemctl enable docker

# Use an official Python runtime as a parent image
FROM python:3.9-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 80 available to the world outside this container (optional, modify if needed)
EXPOSE 8003

# Run the application (modify this to match your Python entry point script)
CMD ["python", "app.py"]