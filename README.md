**Я использовал Python 3.8**


1) `pip install -r requirements.txt`

2) Redis для celery worker
    - Установить Redis
    
    - local celery launch: `celery -A pages worker --loglevel=info`
    
3) `python manage.py migrate`

4) `python manage.py runserver`