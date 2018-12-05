from django.test import RequestFactory
import pytest
from mixer.backend.django import mixer
from django.urls import reverse, resolve
from notice.models import Post
from . import models
from . import views
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone

class Test_urls:
    def test_detail_urls(self):
        path= reverse('post_detail', kwargs={'pk':1})
        assert resolve(path).view_name=='post_detail'
    def test_title(self):
        r=models.Post.title='test name'
        assert 'test name'==r
    def test_author(selfself):
        r=models.Post.author='me'
        assert 'me'==r
    def test_date(self):
        r=models.Post.text="texttext"
        assert r=="texttext"

    @pytest.mark.django_db
    def test_delete(self):
        mixer.blend(Post)
        path = reverse('post_list', kwargs={'pk': 0})
        request = RequestFactory().get(path)
        response = views.post_remove(request, pk=1)
        assert response.status_code == 200

    def test_detail(self):
        path = reverse('post_detail', kwargs={'pk': 0})
        request = RequestFactory().get(path)
        response = views.post_detail(request, pk=0)
        assert response.status_code == 200










