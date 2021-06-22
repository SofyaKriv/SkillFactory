from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView  # импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
from .models import Post, Category
from datetime import datetime
from .filters import PostFilter
from .forms import PostsForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin


@login_required
def upgrade_me(request):
    user = request.user
    premium_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        premium_group.user_set.add(user)
    return redirect('/news/')


class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-id')
    paginate_by = 10

    # метод get_context_data нужен нам для того, чтобы мы могли передать переменные в шаблон. В возвращаемом словаре context будут храниться все переменные. Ключи этого словари и есть переменные, к которым мы сможем потом обратиться через шаблон
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not self.request.user.groups.filter(name='authors').exists()
        context['value1'] = None  # добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        return context

class SearchList(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'search'
    queryset = Post.objects.order_by('-time_creation')
    form_class = PostsForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now

        context['categories'] = Category.objects.all()
        context['form'] = PostsForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса

        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем новый товар
            form.save()

        return super().get(request, *args, **kwargs)


class NewsDetail(DetailView):
    model = Post
    template_name = 'newsdetail.html'
    context_object_name = 'newsdetail'
    queryset = Post.objects.all()


class PostsCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'news.add_post'
    template_name = 'post_create.html'
    form_class = PostsForm
    success_url = '/news/'


# дженерик для редактирования объекта
class PostsUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'news.add_post'
    template_name = 'post_create.html'
    form_class = PostsForm
    success_url = '/news/'

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления товара
class PostsDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'news.delete_post'
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'

