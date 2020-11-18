"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

from django.db import models
from .models import Comment
from .models import Blog

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'style': 'width: 100%;',
                                   'placeholder': 'Логин'}))
    password = forms.CharField(label=_("Пароль"),
                               widget=forms.PasswordInput({
                                   'style': 'width: 100%;',
                                   'placeholder':'Пароль'}))

class FeedbackForm(forms.Form):
    name = forms.CharField(label='Ваше имя', min_length=2, max_length=20)
    email = forms.EmailField(label='E-mail', min_length=7)
    direction = forms.ChoiceField(label='Обращение к', 
                                  choices=[
                                      ('1', 'Поддержка'), 
                                      ('2', 'Маркетинг')
                                      ], widget=forms.RadioSelect, initial=1)
    topic = forms.ChoiceField(label='Тема обращения', choices=(('1', 'Не удается загрузить файл'),
                                                        ('2', 'Удалить аккаунт'),
                                                        ('3', 'Изменить описания файла'),
                                                        ('4', 'Другое')), initial=1)
    check = forms.BooleanField(label='Имеется аккаунт', required=False)
    info = forms.CharField(label='Текст обращения', widget=forms.Textarea(attrs={'rows':4, 'cols':30}))

class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment # используемая модель
        fields = ('text',) # требуется заполнить только поле text
        labels = {'text': "Комментарий"} # метка к полю формы text

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'content', 'file',)
        labels = {'title': "Имя файла", 'description': "Расширение", 'content': "Описание", 'file': "Файл"}