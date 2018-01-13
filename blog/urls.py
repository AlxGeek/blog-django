from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #url('', views.post_list),
    #url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]
