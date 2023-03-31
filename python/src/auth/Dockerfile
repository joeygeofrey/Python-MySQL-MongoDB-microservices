# utilize alpine for a smaller image
FROM python:alpine3.17

LABEL maintener="joeygeof.dev@gmail.com"

RUN apt-get update \
    && apt-get install -y --no-install-recommends --no-install-suggests \
    build-essentials default-libmysqlclient-dev \
    && pip install --no-cache-dir --upgrade pip

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install --no-cache-dir --requirement /app/requirement.txt

COPY . /app/

EXPOSE 5000

CMD ["python3", "server.py"]
    