from .models import Components

from rest_framework import generics
from .serializers import ComponentSerializer


# Crud using REST Framework
class ComponentCreateApi(generics.CreateAPIView):
    queryset = Components.objects.all()
    serializer_class = ComponentSerializer


class ComponentListApi(generics.ListAPIView):
    queryset = Components.objects.all()
    serializer_class = ComponentSerializer


class ComponentUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Components.objects.all()
    serializer_class = ComponentSerializer


class ComponentDeleteApi(generics.DestroyAPIView):
    queryset = Components.objects.all()
