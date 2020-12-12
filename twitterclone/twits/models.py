from django.db import models
from accounts.models import Account
class Twit(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = models.CharField(max_length = 250)
    image = models.FileField(upload_to = 'images/twits/', blank = True)

class Comment(models.Model):
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = models.CharField(max_length = 100)
    twit = models.ForeignKey(Twit, on_delete=models.CASCADE)