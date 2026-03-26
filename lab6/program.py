vi Dockerfile
FROM python:3.10-slim
WORKDIR /app
copy..
Run pip install -r requirements.txt
  CMD["python 3", "app.py"]


