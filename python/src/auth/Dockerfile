# utilize alpine for a smaller image
FROM python:3.12.0a6-slim-bullseye

# set author field
LABEL maintener="joeygeof.dev@gmail.com"

# update and install packages + upgrade pip package manager
RUN apt-get update \
    && apt-get install -y --no-install-recommends --no-install-suggests \
    build-essential default-libmysqlclient-dev \
    && pip install --no-cache-dir --upgrade pip

# designate working directory to /app
WORKDIR /app

# copy dependency requirements to /app
COPY ./requirements.txt /app

# install dependencies
RUN pip install --no-cache-dir --requirement /app/requirements.txt

# copies source code
COPY . /app/

# designate the expected port
EXPOSE 5000

# run the app
CMD ["python3", "server.py"]
    