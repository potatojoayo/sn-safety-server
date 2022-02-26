from django.contrib.postgres.fields import ArrayField
from django.db import models
from user.models import User
from .base_posting import BasePosting

class Posting(models.Model): 

    CATEGORY_CHOICES = [
        ('LECTURE','동영상 강의'),
        ('WATCH', '동영상 시청'),
        ('ANALYSIS', '팀 사례분석'),
        ('DEBRIEFING', '팀 디브리핑'),
        ('PROJECT', '팀 프로젝트'),
        ('DOWNLOAD','학습 자료실'), 
        ('BOARD','열린 게시판'),
        ('QNA', 'Q&A'),
        ('SURVEY', '설문하기')
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    view = models.IntegerField(default=0, blank=True)
    title = models.CharField(max_length=255, null=False)
    date = models.DateTimeField(auto_now_add=True) 
    contents = models.TextField(null=True)
    youtube_id = models.CharField(max_length=255, null=True) 
    meeting_id = models.CharField(max_length=20, null=True)
    survey_url = models.CharField(max_length=200, null=True)
    category = models.CharField(null=False, choices=CATEGORY_CHOICES, max_length=20)
    files = ArrayField( 
        models.CharField(max_length=200)
        ,null=True, blank=True
    )
    download = models.IntegerField(default=0)
    secret = models.BooleanField(default=False)


