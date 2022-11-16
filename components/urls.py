from django.urls import path
from .views import *

app_name = 'computer'

urlpatterns = [
    path('component/create/', ComponentCreateApi.as_view()),
    path('component/list/', ComponentListApi.as_view()),
    path('component/<int:pk>/update/', ComponentUpdateApi.as_view()),
    path('component/<int:pk>/delete/', ComponentDeleteApi.as_view()),

    path('user/create/', UserCreateApi.as_view()),
    path('user/list/', UserListApi.as_view()),
    path('user/<int:pk>/update/', UserUpdateApi.as_view()),
    path('user/<int:pk>/delete/', UserDeleteApi.as_view()),
]

