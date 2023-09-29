# Upload_files_api_drf
 
Django REST API, который позволяет загружать файлы на сервер, а затем асинхронно 
обрабатывать их с использованием Celery. 

Celery обрабатывает загруженный файл и сохраняет его в БД (PostgreSQL). 
В зависимости от типа загруженного файла происходит следующая обработка:
- Для .txt файлов: добавление текста
- Для .jpg файлов: цвет изображения меняется на ч/б
После обработки файла поле processed изменяется на True.

Реализованы следующие эндпоинты:

- 'api/v1/upload' принимает POST-запросы для загрузки файлов.
- 'api/v1/files' возвращает список всех файлов с их данными, включая статус обработки.

### В данном проекте использовались следующие инструменты:
    
  - django v4.2
  - djangorestframework v3.14
  - django-environ v0.11
  - celery v5.3
  - redis v5.0
  - pillow v10.0

##  Настройка и запуск:
1. Перейдите в директорию, в которую будете клонировать репозиторий. Необходимо наличие
установленного и запущенного Docker.
2. Для скачивания репозитория и разворачивания проекта локально в docker контейнере
(создание БД, запуск приложения):

```bash
git clone https://github.com/Vladimir-Ivanov-92/upload_files_api_drf.git
cd upload_files_api_drf 
cd load_files_api_drf
docker-compose up -d --build
```
3. Создайте таблицы в БД:
```bash
docker-compose exec app make migrate
```
4. Запустите Celery:
```bash
docker-compose exec -d app make celery
```
5.  Доступны следующие url:

    http://0.0.0.0:8000/api/v1/files

    http://0.0.0.0:8000/api/v1/upload
