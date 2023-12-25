# Import necessary modules
import os
import django

# Set up Django environment
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "core.settings"
)  # Replace 'your_project_name' with your Django project's settings module
django.setup()

# Import User model from Django's auth module
from django.contrib.auth.models import User  # noqa


def create_superuser():
    # Check if the superuser already exists
    if not User.objects.filter(username="admin").exists():
        # Create a superuser with provided information
        admin_user = User.objects.create_superuser(
            "admin", "admin@example.com", "123456x@X"
        )
        print("Superuser 'admin' created successfully.")
    else:
        print("Superuser 'admin' already exists.")


if __name__ == "__main__":
    create_superuser()
