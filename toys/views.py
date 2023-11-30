from django.shortcuts import render
from .models import Toy
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import ToySerializer
from rest_framework.views import APIView


# Create your views here.

class ToyList(generics.ListCreateAPIView):
    queryset = Toy.objects.all()
    serializer_class = ToySerializer

class ToyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Toy.objects.all()
    serializer_class = ToySerializer
    lookup_field = 'id'
