# Project Structure
```
.
├── django_project
│   ├── core
│   │   ├── asgi.py
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── products
│   │   ├── tests
│   │   │   ├── product_api.py
│   │   │   ├── product_mode.py
│   │   │   └── product_serializer.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── producter.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── scripts
│   ├── consumer.py
│   ├── create_superuser.py
│   ├── Dockerfile
│   ├── manage.py
│   ├── postgres.env
│   ├── README.md
│   └── requirements.txt
├── flask_project
│   ├── app.py
│   ├── config.py
│   ├── consumer.py
│   ├── Dockerfile
│   ├── postgres.env
│   ├── producer.py
│   ├── README.md
│   └── requirements.txt
├── docker-compose.rabbitmq.yml
├── docker-compose.yml
├── rabbitmq.env
└── README.md
```
Contents:
- django_project: Contains the Django project files.
  - core: Core Django project files.
  - products: Django app for handling products.
  - scripts: Scripts related to the Django project.
  - consumer.py: Consumer script.
  - create_superuser.py: Script for creating superuser.
  - Dockerfile: Docker configuration for the Django project.
  - manage.py: Django management script.
  - postgres.env: Environment variables for PostgreSQL.
  - requirements.txt: Required Python dependencies.
  - README.md: Description and instructions for Django project setup.
- flask_project: Contains the Flask project files.
  - app.py: Flask main
  - config.py: Configure flask project
  - consumer.py: Consumer script.
  - producer.py: Pushing script
  - Dockerfile: Docker configuration for the Flask project.
  - postgres.env: Environment variables for PostgreSQL.
  - requirements.txt: Required Python dependencies.
  - README.md: Description and instructions for Flask project setup.
- docker-compose.rabbitmq.yml: Docker Compose file for RabbitMQ setup.
- docker-compose.yml: Main Docker Compose file.
- rabbitmq.env: Environment variables for RabbitMQ.
- README.md: Main README file explaining the project structure and contents.

# Set up

1. cd django_project && cp .env.example .env && cd ..
2. cd flask_project && cp .env.example .env && cd ..
3. docker compose -f docker-compose.rabbitmq.yml up -d --build
4. docker compose up -d --build