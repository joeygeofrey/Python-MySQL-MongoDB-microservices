DOCKER_USERNAME ?= joeygeofrey
APPLICATION_NAME ?= auth

install:
	# run inside a virtual environment
	pip install --no-cache-dir --upgrade setuptools wheel --use-pep517 pip &&\
		pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt
	# Install hadolint
	wget -O /bin/hadolint https://github.com/hadolint/hadolint/releases/download/v2.12.0/hadolint-Linux-x86_64 &&\
    chmod +x /bin/hadolint

lint:
	# lint Dockerfile
	hadolint Dockerfile
	# lint source code
	pylint --disable=C,R1705,W0702 server.py

build:
	docker build --tag ${DOCKER_USERNAME}/${APPLICATION_NAME} .

push:
	docker push ${DOCKER_USERNAME}/${APPLICATION_NAME}

all: install lint build push