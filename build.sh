#!/bin/bash

rm -f dist/*
python setup.py sdist bdist_wheel
tar tzf dist/*.tar.gz
twine check dist/*

# upload to testpypi configured in ~/.pypirc
# twine upload --repository testpypi dist/*
# or: twine upload --repository-url https://test.pypi.org/legacy/ dist/*
# to test install: pip install --index-url https://test.pypi.org/simple/ --no-deps emw_serializer

# upload to pypi configured in ~/.pypirc
twine upload --repository pypi dist/*
