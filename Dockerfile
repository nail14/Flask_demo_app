FROM python:3.9.16

WORKDIR /Flask-project

COPY ./newspapper ./newspapper
COPY ./migrations ./migrations
COPY requirements.txt requirements.txt
COPY wsgi.py wsgi.py

RUN pip3 install -r requirements.txt

RUN flask db upgrade
RUN flask create-admin admin admin@admin.com
RUN flask create-tags

CMD ["gunicorn", "-b", "0.0.0.0:8080",  "wsgi:app"]