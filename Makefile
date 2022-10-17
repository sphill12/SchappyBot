run:
	python main.py

install:
	pip install -r requirements.txt

update: 
	pipreqs . --force