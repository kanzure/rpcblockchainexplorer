SHELL := /bin/bash

test:
	nosetests-2.7 -s -v
	nosetests-3.4 -s -v

clean:
	rm -fr build dist
	rm -fr *.egg-info
	find . -name *.pyc -exec rm {} \;
	find . -name *.swp -exec rm {} \;

install:
	python3.4 setup.py install

upload: clean
	python3.4 setup.py sdist upload
