FROM python:3.7.2 AS development

WORKDIR /usr/src/app/

COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

COPY . /usr/src/app/


FROM development AS production
CMD scripts/start_app.sh