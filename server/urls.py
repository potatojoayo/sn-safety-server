from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from posting.viewsets import *

router = DefaultRouter()
router.register('analysis',AnalysisViewSet,'analysis')
router.register('watch', WatchViewSet, 'watch')
router.register('board',BoardViewSet, 'board')
router.register('download',DownloadViewSet, 'download')
router.register('debriefing',DebriefingViewSet, 'debriefing')
router.register('lecture',PostingViewSet, 'lecture')
router.register('project',ProjectViewSet, 'project')
router.register('qna',QnaViewSet, 'qna')
router.register('survey',SurveyViewSet,'survey')
router.register('watch',WatchViewSet,'watch')
router.register('introduction',IntroductionViewSet,'introduction')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')), 
    path('',include(router.urls)), 
]
