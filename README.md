Requirements
------------
- Python 3.7
- Pipenv
- Redis
- Docker(Runnig Redis)

Setup
------
- Clone Repository
- ``pipenv install``
- ``python manage.py migrate``
- ``python manage.py runserver``
- Start Redis
- ``celery -A assignment worker -B -l info`` [In new termial]
- Navigate to ``localhost:8000``