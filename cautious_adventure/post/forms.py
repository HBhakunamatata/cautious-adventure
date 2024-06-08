from django.forms import ModelForm
from .models import Topic, Post

class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ['topic_cat', 'topic_subject']


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['post_content']