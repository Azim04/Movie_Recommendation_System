# Base Image
FROM python:latest

# Working Directory insde the container
WORKDIR /app

# Installing django into the container
RUN pip install django

# Copy contents from system directory into the container
COPY . /app

# Migrate the users, admins, databases in django (inside the container)
RUN python manage.py migrate

# Open the listening port for the container
EXPOSE 8000

# Start Django Server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
