from rest_framework import serializers
from .models import Question , Solution , Profile


from django.contrib.auth.models import User

from rest_framework import serializers
from django.contrib.auth.models import User

class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"
    def create(self, validated_data):
        # Exclude certain fields from being created
        excluded_fields = ['question_upvotes', 'question_downvotes']
        
        for field in excluded_fields:
            validated_data.pop(field, None)

        return super(QuestionSerializer, self).create(validated_data)
    
class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = "__all__"

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"