# Targets
all: test
test: validate

deps:
	pip3 install -U pip
	pip3 install -r requirements.txt

validate:
	@echo Validating corpora by running:
	./validate.sh
