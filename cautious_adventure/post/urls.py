from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [

    path('', views.query_topics, name="topic-page"),
    path('topic/<str:topic_id>', views.topic_detail, name="topic-detail"),
    path('newTopic/', views.topic_new, name='topic_new'),
    
]