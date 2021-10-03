FROM python:3.9-slim


RUN mkdir /app

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . /app/

ENV PYTHONPATH=/app

EXPOSE 8000

CMD [ "./start_server.sh" ]
