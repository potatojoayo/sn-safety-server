from django.db import models
from .base_posting import BasePosting

class Survey(BasePosting):

    survey_url = models.CharField(max_length=200)
