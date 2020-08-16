# hillel_weather_service

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
