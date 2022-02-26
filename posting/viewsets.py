from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *


class PostingViewSet(ModelViewSet):

    queryset= Posting.objects.all() 
    serializer_class = PostingSerializer

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

