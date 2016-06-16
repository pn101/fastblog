migrate:
	- python fastblog/manage.py makemigrations fastblog posts users bitly
	- python fastblog/manage.py migrate
