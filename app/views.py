"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from .forms import FeedbackForm
from django.contrib.auth.forms import UserCreationForm

from django.db import models
from .models import Blog
from .models import Comment # использование модели комментариев
from .forms import CommentForm # использование формы ввода комментария
from .forms import BlogForm

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    post_all = Blog.objects.all() # запрос на выбор всех статей блога из модели
    post = Paginator(post_all, 5)
    page = request.GET.get('page')
    try:
        posts = post.page(page)
    except PageNotAnInteger:
        posts = post.page(1)
    except EmptyPage:
        posts = post.page(post.num_pages)

    return render(
        request,
        'app/index.html',
        {
            'posts': posts, # педача списка статей в шаблон веб-страницы
            'postCount': post_all.count,
        }

    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
    )

def feedback(request):
    assert isinstance(request, HttpRequest)
    data = None
    direction = {'1': 'Поддержка', '2': 'Маркетинг'}
    topic = {'1': 'Не удается загрузить файл', '2': 'Удалить аккаунт', '3': 'Изменить описания файла', '4': 'Другое'}
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            data = dict()
            data['name'] = form.cleaned_data['name']
            data['email'] = form.cleaned_data['email']
            data['direction'] = direction[ form.cleaned_data['direction'] ]
            data['topic'] = topic[ form.cleaned_data['topic'] ]

            if (form.cleaned_data['check'] == True):
                data['check'] = 'Имеется'
            else:
                data['check'] = 'Отсутствует'
            data['info'] = form.cleaned_data['info']
            form = None
    else:
        form = FeedbackForm()

    return render(
        request,
        'app/feedback.html',
        {
            'form': form,
            'data': data,
        }
    )

def registration(request):
    """Renders the registration page."""
    assert isinstance(request, HttpRequest)

    if request.method == "POST": # после отправки формы
        regform = UserCreationForm (request.POST)
        if regform.is_valid(): #валидация полей формы
            reg_f = regform.save(commit=False) # не сохраняем автоматически данные формы
            reg_f.is_staff = False # запрещен вход в административный раздел
            reg_f.is_active = True # активный пользователь
            reg_f.is_superuser = False # не является суперпользователем
            reg_f.date_joined = datetime.now() # дата регистрации
            reg_f.last_login = datetime.now() # дата последней авторизации
            reg_f.save() # сохраняем изменения после добавления данных
            return redirect('home') # переадресация на главную страницу после регистрации
    else:
        regform = UserCreationForm() # создание объекта формы для ввода данных нового пользователя

    return render(
        request,
        'app/registration.html',
        {
            'regform': regform, # передача формы в шаблон веб-страницы
            'year':datetime.now().year,
        }
    )

def blogpost(request, parametr):
    """Renders the blogpost page."""
    assert isinstance(request, HttpRequest)
    post_1 = Blog.objects.get(id=parametr) # запрос на выбор конкретной статьи по параметру
    comments = Comment.objects.filter(post=parametr)

    if request.method == "POST": # после отправки данных формы на сервер методом POST
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user # добавляем (так как этого поля нет в форме) в модель Комментария (Comment) в поле автор авторизованного пользователя
            comment_f.date = datetime.now() # добавляем в модель Комментария (Comment) текущую дату
            comment_f.post = Blog.objects.get(id=parametr) # добавляем в модель Комментария (Comment) статью, для которой данный комментарий
            comment_f.save() # сохраняем изменения после добавления полей
            return redirect('blogpost', parametr=post_1.id) # переадресация на ту же страницу статьи после отправки комментария
    else:
        form = CommentForm() # создание формы для ввода комментария

    return render(
        request,
        'app/blogpost.html',
        {
            'post_1': post_1, # передача конкретной статьи в шаблон веб-страницы
            'comments': comments, # передача всех комментариев к данной статье в шаблон веб-страницы
            'form': form, # передача формы добавления комментария в шаблон веб-страницы
            'year':datetime.now().year,
        }
    )

def newpost(request):
    assert isinstance(request, HttpRequest)

    if request.method == "POST":
        blogform = BlogForm(request.POST, request.FILES)
        if blogform.is_valid():
            blog_f = blogform.save(commit=False)
            blog_f.posted = datetime.now()
            blog_f.author = request.user
            blog_f.save()

            return redirect('home')
    else:
        blogform = BlogForm()

    return render(
        request,
        'app/newpost.html',
    {
        'blogform': blogform,
        'year':datetime.now().year,
    }
)

def videopost(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/videopost.html',
    )