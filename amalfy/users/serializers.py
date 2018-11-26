from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import User, DayMood

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            'first_name',
            'last_name',
            'is_active',
            'is_superuser',
            'is_staff',
            'last_checked_tip'
        )

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        token = Token.objects.create(user=user)
        return user


class DayMoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = DayMood
        fields = ('date', 'score')