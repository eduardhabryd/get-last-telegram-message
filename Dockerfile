FROM python:3.8-slim

LABEL maintainer = "eduardhabryd@gmail.com"

ENV PYTHONBUFFERED 1

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
