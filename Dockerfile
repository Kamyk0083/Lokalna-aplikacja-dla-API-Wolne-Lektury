FROM python:3.9-slim

WORKDIR /app

COPY app/requirements.txt requirements.txt
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*
RUN pip install -r requirements.txt

COPY app/ /app
COPY app.py /app

EXPOSE 5000

CMD ["python", "app.py"]
