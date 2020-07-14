FROM tiangolo/uwsgi-nginx-flask:python3.8

WORKDIR /app
COPY ./app/requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY ./app .

RUN python ./tests/__init__.py

EXPOSE 80