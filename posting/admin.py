from django.contrib import admin
from .models import *

class PostingAdmin(admin.ModelAdmin):
    pass


class IntroductionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Posting,PostingAdmin)
admin.site.register(Introduction,IntroductionAdmin)
