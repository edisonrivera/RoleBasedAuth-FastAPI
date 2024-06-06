FROM python:latest

RUN apt-get update

WORKDIR /app

COPY . ./

RUN pip install -r requeriments.txt

EXPOSE 8000

WORKDIR /app/app/

CMD ["fastapi", "dev", "./main.py", "--host", "0.0.0.0"]