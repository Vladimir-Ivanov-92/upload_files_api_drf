Project in development...


1. docker-compose up -d --build 
2. docker-compose exec app make migrate
3. docker-compose exec -d app make celery

coverage run --source='.' ./manage.py test upload_files/tests
coverage report