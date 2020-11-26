# Targets
all: test
test: validate

deps:
	pip3 install -U pip
	pip3 install -r requirements.txt

docs:
	@echo Generating documentation by running:
	python ./scripts/make_docs.py

validate:
	@echo Validating corpora by running:
	./scripts/validate.sh
