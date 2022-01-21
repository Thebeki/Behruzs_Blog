from django.urls.conf import include
from django.contrib import admin
from django.urls import path
from rest_framework.generics import CreateAPIView
from .serializers import *
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('post',PostViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path("postlist/<int:pk>", IntroductionView.as_view(), name='postlist'),
    path("postreq/", ListRequestsView.as_view(), name='postrequests'),

]