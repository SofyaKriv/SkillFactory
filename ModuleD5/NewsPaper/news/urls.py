from django.urls import path
from django.conf import settings
from django.conf.urls import url
import allauth.account.views
from .views import NewsList, NewsDetail, SearchList, PostsCreateView, PostsUpdateView, PostsDeleteView, upgrade_me

# LoginView, LogoutView,
# BaseRegisterView

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetail.as_view(), name='newsdetail'),
    path('search/', SearchList.as_view(), name='search'),
    path('create/', PostsCreateView.as_view(), name='post_create'),
    path('create/<int:pk>', PostsUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>', PostsDeleteView.as_view(), name='post_delete'),
    path('accounts/upgrade/', upgrade_me, name='upgrade'),
    # url(r'^logout/$', allauth.account.views.LogoutView, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('accounts/login/', allauth.account.views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # path('logout/', LogoutView.as_view(template_name='sign/logout.html'), name='logout'),
    # path('signup/', BaseRegisterView.as_view(template_name='sign/signup.html'), name='signup'),
]