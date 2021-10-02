FROM python:3
ADD . /v-dj-sample

WORKDIR /v-dj-sample

RUN pip install -r ./requirements/base.txt

EXPOSE 8000

COPY ./docker-entrypoint.sh /
ENTRYPOINT ["sh","/docker-entrypoint.sh"]


#CMD python manage.py runserver 0.0.0.0:8005
