NOSEARGS ?=
DOCKER_TAG ?= latest

VERSION := $(BUILD_NUMBER)
IMAGE_VERSION := v0.$(VERSION)

version:
	@echo "$(IMAGE_VERSION)"

flake8:
	flake8 --max-line-length=120 *.py

start: env flake8
	nohup python web.py &

test: start
	. env/bin/activate
	nosetests -vs $(NOSEARGS)

env: requirements.txt
	@rm -rf env
	@virtualenv env
	@env/bin/pip install -r requirements.txt

clean:
	kill -9 $$(ps -ef | grep web.py | grep -v grep | awk '{print $$2}')  
	rm -rf nohup.out *.pyc


docker-image:
	docker build -t localhost:5000/testweb:$(DOCKER_TAG) .
	docker push localhost:5000/testweb:$(DOCKER_TAG)
	docker tag localhost:5000/testweb:$(DOCKER_TAG) localhost:5000/testweb:$(IMAGE_VERSION)
	docker push localhost:5000/testweb:$(IMAGE_VERSION)

docker-run:
	docker run -it -P --rm --name testweb localhost:5000/testweb

.PHONY: start test env docker-image docker-run clean
