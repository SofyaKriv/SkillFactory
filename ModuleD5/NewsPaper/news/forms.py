from django.forms import ModelForm
from .models import Post, Category
from django import forms
from allauth.account.forms import SignupForm, LoginForm
from django.contrib.auth.models import Group


class BasicSignupForm(SignupForm):
    # premium = forms.BooleanField()

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        # if self.premium:
        #     premium_group = Group.objects.get(name='authors')
        #     premium_group.user_set.add(user)
        return user

class BasicLoginForm(LoginForm):

    def login(self, *args, **kwargs):
        user = super(BasicLoginForm, self).login(*args, **kwargs)
        # basic_group = Group.objects.get(name='basic')
        # basic_group.user_set.add(user)
        return user


# Создаём модельную форму
class PostsForm(ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'title_post', 'category', 'category_type', 'text_post')