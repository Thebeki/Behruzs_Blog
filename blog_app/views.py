
from rest_framework.serializers import Serializer
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import*
from django.views import View
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from .serializers import *

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class IntroductionView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['id', 'title', 'created_on']
    search_fields = ['id', '=title', 'created_on']
    ordering_fields = ['id', 'title', 'created_on']

class ListRequestsView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, ]
    class HomeView(View):
        def get(self, request):
            return render(request, 'index.html')
        def post(self, request):
            u = request.POST.get("login")
            p = request.POST["password"]
            users = authenticate(request, username=u, password=p)
            if users is None:
                return redirect("login")
            else:
                login(request, users)
                return redirect("bolim")

