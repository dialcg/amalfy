from django.contrib.auth import authenticate
from django.shortcuts import render

from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, DayMood
from .serializers import UserSerializer, DayMoodSerializer


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        token = Token.objects.get(key=self.kwargs['token'])
        return token.user


class UserMoodListView(generics.ListAPIView):
    serializer_class = DayMoodSerializer

    def get_queryset(self):
        token = Token.objects.get(key=self.kwargs['token'])
        return DayMood.objects.filter(user=token.user) 


class MoodCreateView(APIView):

    def post(self, request, *args, **kwargs):
        token = request.POST['token']
        mood_score = request.POST['score']
        user = Token.objects.get(key=token).user
        mood = DayMood(
            user=user,
            score=mood_score
        )
        mood.save()
        return Response(status=200)


class Login(APIView):

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            token = Token.objects.get(user=user)
            return Response({'token': token.key})
        return Response(status=400)
