install: clean
	clear; python setup.py build; python setup.py install

release: clean
	@echo "**********************************************"
	@echo "* read ~/installs/pypi.txt before doing this *"
	@echo "**********************************************"
	@read ignore
	cp PyPi_README.rst README.rst
	python3 setup.py sdist bdist_wheel
	twine upload dist/*
	cp github_README.rst README.rst

clean:
	rm -Rf build dist pySlipQt.egg-info/
