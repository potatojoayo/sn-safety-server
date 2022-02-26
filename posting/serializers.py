from rest_framework import serializers
from .models import *

class BaseSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__' 
        extra_kwargs = {'author': {'read_only': True}, 'view': {'read_only': True}}
        depth = 1 
        

class PostingSerializer(BaseSerializer):

    class Meta(BaseSerializer.Meta):
        model = Posting 
        

class IntroductionSerializer(BaseSerializer): 

    profile_image = serializers.SerializerMethodField()

    class Meta(BaseSerializer.Meta):
        model = Introduction 
        

    def get_profile_image(self, obj):
        return 'https://api.sn-safety.kr/assets/'+obj.profile_image.name

class IntroductionWriteSerializer(BaseSerializer):

    class Meta(BaseSerializer.Meta):
        model = Introduction 
        
