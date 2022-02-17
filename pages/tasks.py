from django.db import transaction
from django.db.models import F

from pages.celery import app
from pages.models import Page


@app.task
@transaction.atomic
def increase_counter(page_id):
    page = Page.objects.filter(id=page_id).first()
    page.content.update(counter=F('counter') + 1)
