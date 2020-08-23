# hillel_weather_service

##### Common docker commands

Before building images, create the '.env_bot' file in the 'docker/bot/' directory:
cp .env.example .env_bot
And fill in the required variables.

To build images for web and bot:
docker-compose build --no-cache web bot

To check running containers:
docker-compose ps 

To run containers from images in daemon mode:
docker-compose up -d

To stop running containers:
docker-compose stop

To check container logs:
docker-compose logs --tail=100 -f web 


##### Local deployment
For local deployment use docker-compose-local.yml. It includes the following services:<br>
- web<br>
- bot<br>
- postgres db<br>
- adminer<br>
<br>
First of all, rebuild local images for web and bot. Make sure that .env for web and .env_bot for bot contain up-to-date vars:<br>
```
docker-compose -f docker-compose-local.yml build web bot<br>
```
Up all the services from docker-compose-local.yml:
```
docker-compose -f docker-compose-local.yml up -d
```
Check if containers are running:
```
docker-compose -f docker-compose-local.yml ps
```
