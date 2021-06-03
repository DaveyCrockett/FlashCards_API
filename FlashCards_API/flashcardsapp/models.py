from django.db import models

# Create your models here.


class FlashCard(models.Model):
    term = models.CharField(max_length=50)
    definition = models.CharField(max_length=300)
    collection_id = models.CharField(max_length=50)
