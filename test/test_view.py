
# import fields from django.db.models
from django.db.models import fields
# import serializers from rest_framework
from rest_framework import serializers
# import Views from app.views
from b_api.views import *
# import models from app.models
from b_api.models import *
from django.test import TestCase, Client



class Post_TestViewlists(TestCase): # POST /post
    def setUp(self) -> None:
        """Set up the post viewlists. """
        self.cl = Client() 
        
    def test_post_an_actor(self):
        new = { "id" : 5,
            "title" : "Spider man no way home", 
            "content" : "Spider man no way home coming soon",
            "status" : 1,
            "created_on" : "2021-11-22",
            "updated_on" : "2021-11-22"
            }
        a = self.cl.post('/blog/post/', data=new)
        assert a.status_code == 201
        news = self.cl.get('/blog/post/').data
        assert new is not None
        assert new["id"] is not None
        assert new["title"] == "Spider man no way home"
        assert new["content"] == "Spider man no way home coming soon"
        assert new["status"] == 1
        assert new["created_on"] == "2021-11-22"
        assert new["updated_on"] == "2021-11-22"