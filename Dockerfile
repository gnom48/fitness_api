FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

WORKDIR /src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt

RUN pip install --upgrade -r requirements.txt

EXPOSE 8080

COPY ./app app