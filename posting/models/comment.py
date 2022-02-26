from django.db import models
from user.models import User
from .posting import Posting

class Comment(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, related_name='comments') 
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE, related_name='comments', default=9)
    contents = models.TextField()
    date = models.DateField(auto_now_add=True, blank=True)
