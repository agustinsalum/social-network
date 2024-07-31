
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ..models import Lesson, UserProfile, TakenLesson, Friendship

# Convert your models to JSON

class LessonSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"

class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user']

class FriendshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = "__all__"

class TakenLessonSerializer(ModelSerializer):
    class Meta:
        model = TakenLesson
        fields = "__all__"

class UserLessonSerializer(serializers.ModelSerializer):
    # TakenLesson has a ForeignKey relationship to Lesson
    # Include the complete details of the lesson within the UserLessonSerializer serializer
    lesson = LessonSerializer()

    class Meta:
        model = TakenLesson
        fields = ['lesson']