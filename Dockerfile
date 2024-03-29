FROM --platform=linux/amd64 python:3.11

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=config.docker_settings

WORKDIR /app
COPY requirements*.txt ./
RUN pip install -r requirements.txt
RUN pip install -r requirements.prod.txt

COPY . .

EXPOSE 80

CMD ["gunicorn", "config.wsgi", "-b", "0.0.0.0:80", "--capture-output", "--log-level=info"]
