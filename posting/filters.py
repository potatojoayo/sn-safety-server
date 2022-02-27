from django_filters import rest_framework as filters
from .models import Posting

class PostingFilter(filters.FilterSet):

    class Meta:
        model = Posting
        fields = ('category',)
