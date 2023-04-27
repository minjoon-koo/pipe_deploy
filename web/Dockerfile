FROM python:3.8.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app/web
COPY . .
RUN pip install -r requirements.txt
RUN pip install gunicorn

