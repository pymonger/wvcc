#!/bin/bash

# cleanup
rm -rf flake8.log prospector.log pytest_unit.xml coverage.html/

# run unit tests
pytest --junit-xml=pytest_unit.xml -o junit_family=xunit1

# run linting and pep8 style check (configured by ../.flake8)
flake8 --output-file=flake8.log

# run code coverage
pytest --cov . --cov-report=xml:coverage.xml

# run prospector
prospector > prospector.log
