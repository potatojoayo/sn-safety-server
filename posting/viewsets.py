from django.contrib.auth.models import AnonymousUser
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .models import *
from .serializers import *
from .filters import PostingFilter


class PostingViewSet(ModelViewSet):

    queryset= Posting.objects.all().order_by('-date')
    filterset_class = PostingFilter

    def get_serializer_class(self): 

        if isinstance(self.request.user, AnonymousUser):
            return PostingSerializer
        if self.request.user.is_admin:
            return AdminPostingSerializer
        return PostingSerializer
        
    def get_object(self):
        posting = super().get_object()
        posting.view += 1
        posting.save()
        return posting

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user
        )



class CommentViewSet(ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

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


class UserWatchVideoViewSet(ModelViewSet):

    queryset = UserWatchVideo.objects.all()
    serializer_class = UserWatchVideoSerializer 

    def perform_create(self, serializer):
        serializer.save(
            user = self.request.user
        )

class PostingFilesViewSet(ModelViewSet):

    queryset= PostingFiles.objects.all() 

    def perform_create(self, serializer):
        serializer.save(
            author = self.request.user
        )
    def get_object(self):
        posting_file = super().get_object()
        posting = posting_file.posting
        posting.download += 1
        posting.save()
        return posting_file

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return PostingFilesSerializer 
        else:
            return PostingFileCreateSerializer 

