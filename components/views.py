from .models import Components, Users

from rest_framework import generics
from .serializers import ComponentSerializer, UserSerializer


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


# User model API's

class UserCreateApi(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class UserListApi(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class UserUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class UserDeleteApi(generics.DestroyAPIView):
    queryset = Users.objects.all()
