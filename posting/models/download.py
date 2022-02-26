from django.contrib.postgres.fields import ArrayField
from django.db import models
from .base_posting import BasePosting

class Download(BasePosting): 

    files = ArrayField( 
        models.CharField(max_length=200)
        ,null=True, blank=True
    )
    download = models.IntegerField()




