from django.db import models
from .base_posting import BasePosting

class Debriefing(BasePosting): 

    meeting_id = models.CharField(max_length=20, null=False)


