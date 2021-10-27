from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name = 'index'),
    url('^today/$',views.news_of_day,name='newsToday')
]
