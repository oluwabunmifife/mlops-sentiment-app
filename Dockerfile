# Specifying the platform since I'm building the image on a Mac
FROM --platform=linux/amd64 python:3.13 AS build_amd64
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY ./app ./app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]