from django.db import models

class Account(models.Model):
    login = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)
    image = models.FileField(upload_to = 'images/accounts/', blank = True)
    follows = models.ManyToManyField('self', blank=True)
