from rest_framework import serializers
from .models import *
from user.serializers import UserSerializer

class BaseSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__' 
        extra_kwargs = {'author': {'read_only': True}, 'view': {'read_only': True}}
        depth = 1 

class PostingFilesSerializer(serializers.ModelSerializer): 

    class Meta:
        model =  PostingFiles
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        file = 'https://api.sn-safety.kr/assets/'+instance.file.name
        representation['link']=file 
        representation['name']=instance.file.name
        return representation

        
class CommentSerializer(serializers.ModelSerializer): 

    author = UserSerializer(read_only=True)
    class Meta:
        model = Comment 
        fields = '__all__'
        extra_kwargs = {'author': {'read_only': True}, 'date': {'read_only': True}} 

class PostingSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True, read_only=True) 
    posting_files = PostingFilesSerializer(many=True, read_only=True)

    class Meta:
        model = Posting 
        fields = '__all__' 
        extra_kwargs = {'author': {'read_only': True}, 'view': {'read_only': True}, 'posting_files': {'read_only':True}}
        depth = 1 
        

class IntroductionSerializer(BaseSerializer): 

    profile_image = serializers.SerializerMethodField()

    class Meta(BaseSerializer.Meta):
        model = Introduction 
        

    def get_profile_image(self, obj):
        return 'https://api.sn-safety.kr/assets/'+obj.profile_image.name

class IntroductionWriteSerializer(BaseSerializer):

    class Meta(BaseSerializer.Meta):
        model = Introduction 
        

class UserWatchVideoSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = UserWatchVideo
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True}}
        

    def create(self, validated_data):

        user_watch_video = UserWatchVideo.objects.filter(user = self.context['request'].user, posting=validated_data['posting']).first()
        if user_watch_video is not None: 
            user_watch_video.percentage += validated_data['percentage']
            user_watch_video.save()
            return user_watch_video
        user_watch_video, _ = UserWatchVideo.objects.update_or_create(**validated_data)
        return user_watch_video 


class AdminPostingSerializer(BaseSerializer):

    comments = CommentSerializer(many=True, read_only=True) 
    user_watch_video = UserWatchVideoSerializer(many=True, read_only=True)
    posting_files = PostingFilesSerializer(many=True, read_only=True)

    class Meta(BaseSerializer.Meta):
        model = Posting 


class PostingFileCreateSerializer(BaseSerializer):

    class Meta:
        model = PostingFiles 
        fields = ('posting','file')


