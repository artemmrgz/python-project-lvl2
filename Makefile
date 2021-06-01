install:
	poetry install


build:
	poetry build


publish:
	poetry publish --dry-run


package-install:
	python3 -m pip install --user dist/*.whl


lint:
	poetry run flake8 gendiff


coverage:
	poetry run coverage run -m pytest
	poetry run coverage xml
