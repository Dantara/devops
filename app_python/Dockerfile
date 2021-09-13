FROM python:3-alpine

WORKDIR /app

RUN adduser -D docker_user && chown -R docker_user /app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY ./app.py .

USER docker_user

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
