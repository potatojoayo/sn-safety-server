from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *

class AnalysisViewSet(ModelViewSet):

    queryset = Analysis.objects.all()
    serializer_class = AnalysisSerializer 
    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user
        )
 

class BoardViewSet(ModelViewSet):

    queryset= Board.objects.all()
    serializer_class = BoardSerializer
    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user
        )

class DebriefingViewSet(ModelViewSet):

    queryset = Debriefing.objects.all()
    serializer_class = DebriefingSerializer
    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user
        )

class DownloadViewSet(ModelViewSet):

    queryset= Download.objects.all() 
    serializer_class = DownloadSerializer
    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user
        )

class PostingViewSet(ModelViewSet):

    queryset= Posting.objects.all() 
    serializer_class = PostingSerializer

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user
        )

class ProjectViewSet(ModelViewSet):

    queryset= Project.objects.all() 
    serializer_class = ProjectSerializer
    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user
        )

class QnaViewSet(ModelViewSet):

    queryset= QnA.objects.all() 
    serializer_class = QnaSerializer
    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user
        )

class SurveyViewSet(ModelViewSet):

    queryset= Survey.objects.all() 
    serializer_class = SurveySerializer
    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user
        )


class WatchViewSet(ModelViewSet):

    queryset= Watch.objects.all() 
    serializer_class = WatchSerializer
    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user
        )

class IntroductionViewSet(ModelViewSet):

    queryset= Introduction.objects.all() 
    serializer_class =IntroductionSerializer 

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return IntroductionSerializer
        else:
            return IntroductionWriteSerializer

