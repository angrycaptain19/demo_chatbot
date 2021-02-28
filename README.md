## Setup Steps

1. `rasa shell --debug`
2. `rasa run actions -vv`
3. `docker build -t mysql-example -f docker/mysql/Dockerfile .`   
3. `docker run -e MYSQL_ROOT_PASSWORD=yourpassword -P mysql-example`
4. `docker run -d -p 8000:8000 rasa/duckling:latest`

Note: Please change the mysql password and modify PWD constant available in `actions/constants` location