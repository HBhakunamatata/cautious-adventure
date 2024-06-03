
5月28日

1. 修改homebrew代码源（阿里—清华）
2. homebrew安装mysql@8.0 root Hb@85701729
3. Form js提交 自己创建表单。。


2024-05-31

## 1.1 ImportError: doesn’t look like a module path
网上查询到的解答都不是我的问题所在，这样的错误应该是属于一大类错误，需要很具自己的代码找原因，主要问题还是在django的settings上。

## 1.2 Django Issue

Application cascade
Template cascade
Urls cascade

Static element collect (
 Html — template
 Css js img
)

## 1.3 static file access (Development)

https://docs.djangoproject.com/en/3.2/howto/static-files/

app: staticfile
file: settings.py

- For assets directory for entire project

```
STATICFILES_DIRS = [
    BASE_DIR / "static",
    '/var/www/static/',
]
```

- For applications

```
STATIC_URL = '/static/'
```


2024-06-01

## 1.4 makemigrations failed 

install mysql driver  

```
pip install mysql-client==2.1
```

## 1.4 avoid publishing secret message

I would try to avoid declaring variables in .bash_profile and would instead create .ini file inside your project (add it .gitignore if you use git) where you will put all your secret variables and use tool like Python-Decouple.

https://github.com/HBNetwork/python-decouple

```
# put the settings.ini or settings.env file next to the module (the root of repo directory)
[settings]
DEV_DB_NAME = cautious-adventure-dev
DEV_DB_USERNAME = 
DEV_DB_PASSWORD = 
DEV_DB_HOST = 127.0.0.1
DEV_DB_PORT = 3306
```

## 1.5 connect to mysql

In settings.py, user the params defined in .ini file using python-decouple

```python
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DEV_DB_NAME'),
        'USER': config('DEV_DB_USERNAME'),
        'PASSWORD': config('DEV_DB_PASSWORD'),
        'HOST': config('DEV_DB_HOST'),
        'PORT': config('DEV_DB_PORT'),
    }
}
```

## 1.6 connect db failed

1. django.db.utils.operationalerror:<1045,”access denied for user root@localhost using password yes>  

Reason: username or password error


## 1.7 liquid filter and foreigner key set

```
{% for post in topic.post_set.all %}
<p>creator name1 published in <time>{{post.create_time|date:'Y-m-d H:i'}}</time></p>
```

## 1.8 Form frontend page template

```html
<div>
    <a href="{% url 'topic-page' %}"><button>Back</button></a>
    <form method="post">
        {% csrf_token %}

        {% for field in form %}
            <label for="{{field.label}}">{{field.label}}</label>
            {{field}}
        {% endfor %}
        <button type="submit">Submit</button>
    </form>
</div>
```

## 1.2 CRUD

### 1.2.1 Create

```python
def topic_new(request):
    """
    Get: give the page of topic form unfilled
    POST: validate the topic form data and create 
    """
    topicForm = TopicForm()

    if request.method == 'POST':
        topicForm = TopicForm(request.POST)
        if topicForm.is_valid():
            topicForm.save()
            return redirect('topic-page')

    context = {'form': topicForm}
    return render(request, 'post/topic-form.html', context)
```