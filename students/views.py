from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializer, CourseSerializer
from .models import User, Course
from .paginators import UserPagination
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()
    pagination_class = UserPagination

    def get_queryset(self):
        return self.queryset.order_by('last_name', 'first_name', 'date_joined')


class CourseViewSet(viewsets.ModelViewSet):

    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = UserPagination