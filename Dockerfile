FROM tiangolo/uwsgi-nginx-flask:python3.8

WORKDIR /app
COPY ./app/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY ./app .

EXPOSE 80