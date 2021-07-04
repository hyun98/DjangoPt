FROM python:3.9.0

WORKDIR /home/

RUN echo "testing1"

RUN git clone https://github.com/hyun98/DjangoPt.git

WORKDIR /home/DjangoPt/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=config.settings.deploy &&\
      python manage.py migrate --settings=config.settings.deploy && \
      gunicorn --bind 0.0.0.0:8000 config.wsgi:application --env DJANGO_SETTINGS_MODULE=config.settings.deploy"]
