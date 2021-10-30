from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name = 'index'),
    url('^profile/$',views.profile,name='profile'),
]
