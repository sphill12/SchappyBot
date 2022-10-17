run:
	@python main.py

install:
	pip install -r requirements.txt
	pre-commit install

update: 
	pipreqs . --force
