# Dockerfile

# Python parent image
FROM python:3.8-slim

# Install curl
RUN apt-get update && apt-get install -y curl

# Set working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install packages specified in requirements.txt
RUN pip install -r requirements.txt 

# Make port 80 available 
EXPOSE 5000

# Define environment variable
ENV NAME World

CMD ["python", "app.py"]

