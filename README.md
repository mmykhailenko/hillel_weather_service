# hillel_weather_service

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
