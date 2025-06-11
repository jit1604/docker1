# Use the official Python image from Docker Hub
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy all files from your project folder into the container
COPY . .

# Run the Python script
CMD ["python", "pythonproj.py"]
