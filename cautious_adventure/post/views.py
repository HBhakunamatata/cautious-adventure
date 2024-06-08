from django.shortcuts import redirect, render
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Post, Topic, Category
from .forms import TopicForm, PostForm

# Create your views here.

def query_topics(request):
    """query posts in terms of condition which user input"""
    if request.method == 'GET':
        print(request.GET)
        search_param = request.GET.get('search_param')
        if search_param is None:
            search_param = ""
    # print("search_param: " + str(search_param))
    topics = condition_query_topic(search_param)

    ## pagination
    page_no = request.GET.get('page_no')
    page_size = 2
    page_topics, page_range = paginate_topic(page_no, page_size, topics)
    # print(page_topics)
    context = {'page_topics': page_topics, 'page_range': page_range}
    return render(request, 'post/topic-page.html', context)


def condition_query_topic(search_param):
    category_set = Category.objects.filter(cat_name__icontains=search_param)
    topics = Topic.objects.distinct().filter(
        Q(topic_subject__icontains=search_param) |
        Q(topic_cat__in=category_set)
    )
    return topics


def get_page_range(page_no, num_pages, page_size=0):
    """TODO: use page_size to calculate page_range"""
    # half_range = int(page_size / 2)
    start_index = int(page_no) - 4
    if start_index < 1:
        start_index = 1
    end_index = int(page_no) + 5 
    if end_index > num_pages:
        end_index = num_pages
    return range(start_index, end_index + 1)


def paginate_topic(page_no, page_size, topic_set):
    """paginate topic search set"""
    paginator = Paginator(topic_set, page_size)
    try:
        paginator.page(page_no)
    except EmptyPage:
        page_no = 1
    except PageNotAnInteger:
        page_no = 1
    result = paginator.page(page_no)
    page_range = get_page_range(page_no, paginator.num_pages)
    return result, page_range


def topic_detail(request, topic_id):
    """
    Get subject of topic and posts according to @param topic_id.
    Response to the creation of new post request
    """
    select_topic = Topic.objects.get(topic_id=topic_id)
    post_form = PostForm()

    # create a new post
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.post_topic = select_topic
            profile = request.user.profile
            new_post.post_by = profile
            new_post.save()
            messages.success(request, "Post was created sucessfully!")
            return redirect('topic-detail', select_topic.topic_id)
        else:
            print('post form is valid.')

    context = {'topic': select_topic, 'post_form': post_form}
    return render(request, 'post/topic-post.html', context)


@login_required
def topic_new(request):
    """
    Get: give the page of topic form unfilled
    POST: validate the topic form data and create 
    """
    topicForm = TopicForm()

    if request.method == 'POST':
        topicForm = TopicForm(request.POST)
        if topicForm.is_valid():
            new_topic = topicForm.save(commit=False)
            user = request.user
            new_topic.topic_by = user.profile
            new_topic.save()
            messages.success(request, "Topic was created sucessfully!")
            return redirect('topic-page')
        else:
            messages.error(request, "Topic message is missed maybe try again later.")

    context = {'form': topicForm}
    return render(request, 'post/topic-form.html', context)


@login_required
def topic_update(request, pk):
    """update topic"""
    profile = request.user.profile
    select_topic = profile.topic_set.get(topic_id=pk)
    form = TopicForm(instance=select_topic)
    
    if request.method == 'POST':
        form = TopicForm(request.POST, instance=select_topic)
        if form.is_valid():
            form.save()
            return redirect('profile')

    context = {'form': form}
    return render(request, 'post/topic-form.html', context)


@login_required
def topic_delete(request, pk):
    """delete the topic"""
    if request.method == 'POST':
        profile = request.user.profile
        select_topic = profile.topic_set.get(topic_id=pk)
        select_topic.delete()
        return redirect('profile')
    return render(request, 'post/topic-delete-form.html')