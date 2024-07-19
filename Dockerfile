# Use the official Python image from the Docker Hub
FROM python:3.9-alpine3.13
LABEL maintainer="tejas1610"

# Set environment variables
ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt

# Copy application code
COPY ./app /app

# Set the working directory
WORKDIR /app
EXPOSE 8000

ARG DEV=false
# Create a virtual environment and install dependencies
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true"]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi &&\
    rm -rf /tmp

RUN pip install flake8

# Add a non-root user for running the application
RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

ENV PATH="/py/bin:$PATH"

 # Set the user to django-user
USER django-user