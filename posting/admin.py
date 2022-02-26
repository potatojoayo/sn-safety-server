from django.contrib import admin
from .models import *

class AnalysisAdmin(admin.ModelAdmin):
    pass

class WatchAdmin(admin.ModelAdmin):
    pass

class PostingAdmin(admin.ModelAdmin):
    pass

class DebriefingAdmin(admin.ModelAdmin):
    pass

class ProjectAdmin(admin.ModelAdmin):
    pass

class BoardAdmin(admin.ModelAdmin):
    pass

class QnaAdmin(admin.ModelAdmin):
    pass

class SurveyAdmin(admin.ModelAdmin):
    pass

class IntroductionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Analysis,AnalysisAdmin)
admin.site.register(Watch,WatchAdmin)
admin.site.register(Posting,PostingAdmin)
admin.site.register(Debriefing,DebriefingAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Board,BoardAdmin)
admin.site.register(QnA,QnaAdmin)
admin.site.register(Survey,SurveyAdmin)
admin.site.register(Introduction,IntroductionAdmin)
