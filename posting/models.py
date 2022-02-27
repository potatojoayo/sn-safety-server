from user.models import User
from django.contrib.postgres.fields import ArrayField
import datetime
from django.db import models
from user.models import User

def upload_to(instance, filename):
    now = datetime.datetime.now()
    now = now.strftime('%Y-%m-%d_%H%M')
    filebase, extension = filename.split('.')
    return '{}.{}'.format(filebase+'-'+now,extension)

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
    contents = models.TextField(null=True, blank=True)
    youtube_id = models.CharField(max_length=255, null=True) 
    meeting_date = models.DateTimeField(null=True, blank=True)
    meeting_id = models.CharField(max_length=20, null=True)
    survey_url = models.CharField(max_length=200, null=True)
    category = models.CharField(null=False, choices=CATEGORY_CHOICES, max_length=20)
    '''    files = ArrayField( 
        models.FileField(upload_to=upload_to)
        ,null=True, blank=True
    )
''' 
    download = models.IntegerField(default=0, null=False)
    secret = models.BooleanField(default=False)





class UserWatchVideo(models.Model):

    posting = models.ForeignKey(Posting, on_delete=models.CASCADE, related_name='user_watch_video')
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True)
    percentage = models.IntegerField()

    class Meta:
        unique_together = ('posting','user')


class Introduction(models.Model): 

    title = models.CharField(max_length=100)
    course_introduction = models.TextField()
    instructor_introduction= models.CharField(max_length=200) 
    instructor_name = models.CharField(max_length=10)
    profile_image = models.ImageField(null=True, blank=True, upload_to=upload_to)
    job = models.CharField(max_length=100)



class Comment(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, related_name='comments',null=True) 
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE, related_name='comments', default=9)
    contents = models.TextField()
    date = models.DateTimeField(auto_now_add=True, blank=True)

class PostingFiles(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, related_name='posting_files',null=True) 
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE, related_name='posting_files')
    file = models.FileField()

