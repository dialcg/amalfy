from django.shortcuts import render
from rest_framework import generics
from .models import Tip
from .serializers import TipSerializer


class TipListView(generics.ListAPIView):
    queryset = Tip.objects.all()
    serializer_class = TipSerializer


class TipDetailView(generics.RetrieveAPIView):
    queryset = Tip.objects.all()
    serializer_class = TipSerializer
        