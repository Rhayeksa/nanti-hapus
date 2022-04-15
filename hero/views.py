from django.shortcuts import render
from rest_framework import generics, permissions, viewsets, filters

from hero.models import Hero
from hero.serializers import Serializer


# Create your views here.


class ListCreateAPIViewHero(viewsets.ViewSetMixin, generics.ListCreateAPIView):
    queryset = Hero.objects.all()
    serializer_class = Serializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nama']
    ordering_fields = ['id', 'nama', 'role']
    # permission_classes = [permissions.IsAuthenticated]


class RetrieveUpdateDestroyAPIViewHero(viewsets.ModelViewSet, generics.RetrieveUpdateDestroyAPIView):
    queryset = Hero.objects.all()
    serializer_class = Serializer
    # permission_classes = [permissions.IsAuthenticated]
