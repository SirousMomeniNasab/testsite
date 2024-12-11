# Use the official Python 3.9 image as the base image
FROM python

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements.txt file into the container at the current working directory (/app)
COPY requirements.txt .

# Install the dependencies specified in requirements.txt using pip
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container at the current working directory (/app)
COPY . /app

# Collect static files

# Run database migrations

# Expose port 8000 to the host machine, allowing incoming connections
EXPOSE 8000

# Set the default command to run when the container starts, which is to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]