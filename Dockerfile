FROM django
ADD . /v-dj-sample

WORKDIR /v-dj-sample

RUN pip install -r ./requirements/base.txt

EXPOSE 8000

COPY ./docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]


#CMD python manage.py runserver 0.0.0.0:8005
