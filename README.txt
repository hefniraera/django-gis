# Django GIS Project

## Description
This project is a Django application to manage Culinary Spots data with GIS features using PostgreSQL + PostGIS.  
The Admin interface includes filters, search functionality, and custom __str__ implementations for the models.

## How to Set Up the Project

1. Clone this repository:

git clone https://github.com/hefniraera/django-gis.git
cd django-gis


2. Create and activate a virtual environment (optional but recommended):
- On Linux/Mac:
  ```
  python3 -m venv env
  source env/bin/activate
  ```
- On Windows (PowerShell):
  ```
  python -m venv env
  .\env\Scripts\Activate.ps1
  ```

3. Install dependencies:
pip install -r requirements.txt


4. Create a `.env` file in the project root (next to `manage.py`) with the required environment variables, for example:
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432

5. Run migrations to create database tables:
python manage.py migrate

6. Create a superuser (admin):
python manage.py createsuperuser

7. Run the development server:
python manage.py runserver

8. Access the Django admin interface at:
http://127.0.0.1:8000/admin/

