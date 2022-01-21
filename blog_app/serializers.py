from django.db.models import fields
from rest_framework import serializers
from .import models
from rest_framework.exceptions import ValidationError

class PostSerializer(serializers.ModelSerializer):
    class Meta: 
        model = models.Post
        fields = '__all__'
