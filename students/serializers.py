from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):

    """
    users field is rewritten in order to apply required ordering
    """

    users = serializers.SerializerMethodField('get_users')

    class Meta:
        model = Course
        fields = '__all__'

    def get_users(self, obj):
        users = obj.users.all().order_by('last_name', 'first_name', 'date_joined')
        serializer = UserSerializer(users, many=True)
        return serializer.data