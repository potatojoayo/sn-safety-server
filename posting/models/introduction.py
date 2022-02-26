from django.db import models
import datetime

def upload_to(instance, filename):
    now = datetime.datetime.now()
    now = now.strftime('%Y-%m-%d_%H%M')
    filebase, extension = filename.split('.')
    return 'assets/{}.{}'.format(filebase+'-'+now,extension)

class Introduction(models.Model): 

    title = models.CharField(max_length=100)
    course_introduction = models.TextField()
    instructor_introduction= models.CharField(max_length=200) 
    instructor_name = models.CharField(max_length=10)
    profile_image = models.ImageField(null=True, blank=True, upload_to=upload_to)
    job = models.CharField(max_length=100)






