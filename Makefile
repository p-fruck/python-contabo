.PHONY: all clean build install test

all: clean build install test

clean:
	./custom/clean.sh

build:
	./custom/build.sh

install:
	pip install -r requirements*.txt

test: # No functionality in unit-tests, they just validate that all files have valid syntax :)
	python -m unittest
