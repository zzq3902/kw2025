import os.path

from django.db import models

# Create your models here.


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.title
