from django.contrib.postgres.fields import ArrayField
from django.db import models
from .base_posting import BasePosting

class Project(BasePosting): 

    files = ArrayField( 
        models.CharField(max_length=200), blank=True, null=True
    )




