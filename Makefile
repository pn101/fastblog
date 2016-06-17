migrate:
	- python fastblog/manage.py makemigrations fastblog posts users bitly
	- python fastblog/manage.py migrate

test:
	- python fastblog/manage.py test fastblog posts users bitly

pep:
	- pep8 .
