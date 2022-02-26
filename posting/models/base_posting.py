from django.db import models
from user.models import User
import datetime

class BasePosting(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    view = models.IntegerField(default=0, blank=True)
    title = models.CharField(max_length=255, null=False)
    date = models.DateTimeField(auto_now_add=True) 
    contents = models.TextField()

    class Meta:
        abstract = True

