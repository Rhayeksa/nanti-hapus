from django.shortcuts import render
from rest_framework import viewsets, generics, filters, permissions
from orang.models import Orang

from orang.serializers import Serializer
# Create your views here.


class ListCreateAPIViewOrang(viewsets.ViewSetMixin, generics.ListCreateAPIView):
    queryset = Orang.objects.all()
    serializer_class = Serializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nama']
    ordering_fields = ['id', 'nama', 'id_hero']
    # permission_classes = [permissions.IsAuthenticated]


class RetrieveUpdateDestroyAPIViewOrang(viewsets.ModelViewSet, generics.RetrieveUpdateDestroyAPIView):
    queryset = Orang.objects.all()
    serializer_class = Serializer
    # permission_class = [permissions.IsAuthenticated]
