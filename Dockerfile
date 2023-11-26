# Use an official Python runtime as a parent image
FROM python:latest

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
RUN mkdir /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Collect static files (if needed)
# RUN python manage.py collectstatic --noinput

# Expose the port the application runs on
EXPOSE 80

# Start the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]