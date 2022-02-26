from django.db import models
from .base_posting import BasePosting

class Watch(BasePosting): 

    youtube_id = models.CharField(max_length=255, null=False) 


