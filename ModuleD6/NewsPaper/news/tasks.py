from django.core.mail import send_mail
import datetime
from .models import User, Post
from django.template.loader import render_to_string


def send_mails():
    end_date = datetime.datetime.now().date()
    start_date = end_date - datetime.timedelta(days=7)
    print('Выполнение началось')
    for user in User.objects.all():
        email = user.email
        if len(user.category_set.all()) > 0:
            list_of_posts = Post.objects.filter(time_creation__range=(start_date, end_date),
                                                category__in=user.category_set.all())
            html_content = render_to_string(
                'sub_week.html',
                {
                    'news': list_of_posts,
                    'user': user,
                }
            )
            send_mail(
                    subject="Новые статьи за неделю",
                    message=f'{user}, в Вашей любимой категории новые статьи.',
                    from_email='test250621@yandex.ru',
                    recipient_list=[email],
                    html_message=html_content
            )
    # print("Hello from scheduler")