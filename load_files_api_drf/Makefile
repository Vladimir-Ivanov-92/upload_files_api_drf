###### comands only for local:
db_up:
	docker compose -f docker-compose-local.yml up -d --build && sleep 5 && python manage.py migrate

db_down:
	docker compose -f docker-compose-local.yml down

celery_up:
	mkdir logs && brew services start redis && nohup celery -A load_files_api_drf worker -l INFO >logs/output.log 2>&1 &

celery_down:
	pkill -f 'celery -A load_files_api_drf worker' && rm -r logs && brew services stop redis

###### comands only for docker:
migrate:
	python manage.py migrate

celery:
	celery -A load_files_api_drf worker -l INFO




#test:
#	docker exec -it app bash -c "pytest . -v"
#
#run_stored_pocedure:
#	docker exec -it app bash -c "python3 run_stored_procedure.py"