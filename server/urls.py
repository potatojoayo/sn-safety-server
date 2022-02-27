from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from posting.viewsets import *

router = DefaultRouter()
router.register('posting',PostingViewSet, 'posting')
router.register('introduction',IntroductionViewSet,'introduction')
router.register('comment',CommentViewSet,'comment')
router.register('watch',UserWatchVideoViewSet,'watch')
router.register('files',PostingFilesViewSet,'files')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')), 
    path('',include(router.urls)), 
]
