from django.db import models
from .base_posting import BasePosting

class QnA(BasePosting):
    secret = models.BooleanField(default=False)
