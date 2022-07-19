from datetime import datetime
from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Posts(models.Model):
    text = models.TextField(max_length=290, default='')
    datetime = models.DateTimeField(default= datetime.now)
    uname = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.uname)

  
class profile(models.Model):
    pass