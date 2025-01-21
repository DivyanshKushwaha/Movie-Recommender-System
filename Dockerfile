# Use a lightweight Python 3.10 image
FROM python:3.10-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy the necessary files from the host to the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy only the necessary files to the container (ignoring unnecessary files via .dockerignore)
COPY . /app/

# Expose the port that the Flask app will run on
EXPOSE 5000

# Command to run the Flask app
CMD ["python", "app.py"]



