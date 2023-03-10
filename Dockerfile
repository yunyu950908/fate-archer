# Use an official Python runtime as a parent image
FROM python:3.11-slim-bullseye

RUN apt-get update && apt-get install -y build-essential

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set the environment variable for Flask
ENV FLASK_APP=app.py
ENV OPENAI_EMAIL=$OPENAI_EMAIL
ENV OPENAI_PASSWORD=$OPENAI_PASSWORD
ENV REDIS_HOST=$REDIS_HOST
ENV TZ=Asia/Shanghai

# Expose the port that the Flask app will run on
EXPOSE 5000

# Start the Flask app when the container starts
CMD ["flask", "run", "--host=0.0.0.0"]
