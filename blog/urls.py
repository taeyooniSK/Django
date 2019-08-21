from django.urls import path  # path는 장고의 함수
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
