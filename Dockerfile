# Use an official Python runtime as a base image
FROM python:3.9-slim-bullseye

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Upgade pip
RUN pip install --upgrade pip

# Install any needed updates
RUN apt-get update && apt-get upgrade -y 

# Install any needed packages
RUN apt-get install -y build-essential libssl-dev libffi-dev python3-dev
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME AutoGenContainer

# Run app.py when the container launches
CMD ["python", "app.py"]
