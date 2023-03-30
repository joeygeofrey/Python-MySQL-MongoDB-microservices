install:
		# run inside a virtual environment
		pip install --no-cache-dir --upgrade setuptools wheel --use-pep517 pip &&\
			pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

lint:
		# run inside a virtual environment
		pylint server.pylint

all: install lint