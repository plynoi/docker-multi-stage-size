# Dockerfile multi-stage build with Python Pip
# Common Image
FROM python:3.8.11-alpine AS alpine
# Builder Stage
#FROM python:3.8.11-alpine as builder
FROM alpine as builder
COPY requirements.txt .
# install dependencies to the local user directory (eg. /root/.local)
RUN pip install --user -r requirements.txt

# Running Stage
FROM alpine  
WORKDIR /app

# copy only the dependencies installation from the 1st stage image
COPY --from=builder /root/.local /root/.local

# update PATH environment variables 
# Set Docker and Applications Env  
# set Python buffer to make Docker print every message instantly.
ENV PATH=/root/.local:$PATH \ 
    USER=PYTHON_PIP_MULTISTAGE \
    PYTHONUNBUFFERED=1

# Copy SRC
COPY src/ .
# Running application
CMD ["python","app.py"]