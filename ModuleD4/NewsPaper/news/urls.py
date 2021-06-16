from django.urls import path
from .views import NewsList, NewsDetail, SearchList, PostsCreateView, PostsUpdateView, PostsDeleteView  # импортируем наше представление

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetail.as_view(), name='newsdetail'),
    path('search/', SearchList.as_view(), name='search'),
    path('create/', PostsCreateView.as_view(), name='post_create'),
    path('create/<int:pk>', PostsUpdateView.as_view(), name='post_update'),
    path('delete/<int:pk>', PostsDeleteView.as_view(), name='post_delete')
]