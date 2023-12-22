# Create RabitMQ server online
1. https://www.cloudamqp.com/
# Enter the input value in .env file
2. cp .env.example .env
# Start docker
2. docker compose up -d --build
3. docker exec -it <your_django_container_name> bash
4. python manage.py createsuperuser
5. exit