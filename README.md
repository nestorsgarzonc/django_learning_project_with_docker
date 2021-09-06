docker-compose run web django-admin startproject composeexample .
docker-compose up
docker-compose down
docker ps
docker-compose run web python3 manage.py migrate
docker-compose run web python3 manage.py makemigrations