from rest_framework import serializers
from .models import *

class BaseSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__' 
        extra_kwargs = {'author': {'read_only': True}, 'view': {'read_only': True}}
        depth = 1



class AnalysisSerializer(BaseSerializer):

    class Meta(BaseSerializer.Meta):
        model = Analysis 
         

class BoardSerializer(BaseSerializer):

    class Meta(BaseSerializer.Meta):
        model = Board 
        

class DebriefingSerializer(BaseSerializer):

    class Meta(BaseSerializer.Meta):
        model = Debriefing 
        

class DownloadSerializer(BaseSerializer):

    class Meta(BaseSerializer.Meta):
        model = Download 
        

class PostingSerializer(BaseSerializer):

    class Meta(BaseSerializer.Meta):
        model = Posting 
        fields = '__all__' 
        extra_kwargs = {'author': {'read_only': True}, 'view': {'read_only': True}}
        depth = 1

class ProjectSerializer(BaseSerializer):

    class Meta(BaseSerializer.Meta):
        model = Project 
        

class QnaSerializer(BaseSerializer):

    class Meta(BaseSerializer.Meta):
        model = QnA 
        

class SurveySerializer(BaseSerializer):

    class Meta(BaseSerializer.Meta):
        model = Survey 
        


class WatchSerializer(BaseSerializer):

    class Meta(BaseSerializer.Meta):
        model = Watch 
        

class IntroductionSerializer(BaseSerializer): 

    profile_image = serializers.SerializerMethodField()

    class Meta(BaseSerializer.Meta):
        model = Introduction 
        

    def get_profile_image(self, obj):
        return 'https://api.sn-safety.kr/assets/'+obj.profile_image.name

class IntroductionWriteSerializer(BaseSerializer):

    class Meta(BaseSerializer.Meta):
        model = Introduction 
        
