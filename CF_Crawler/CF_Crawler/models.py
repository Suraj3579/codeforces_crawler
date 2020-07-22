from django.db import models


# Create your models here.
class Query(models.Model):
    user_name = models.CharField(max_length=30)
    user_email = models.CharField(max_length=50)
    query_subject = models.CharField(max_length=50)
    query_text = models.CharField(max_length=200)
