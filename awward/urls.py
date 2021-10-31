from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns=[
    url(r'^$',views.index,name = 'index'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^project/(\d+)/$', views.project, name='project'),
    url(r'^accounts/register/complete/$', views.edit_profile, name='edit_profile'),
    url(r'^search/', views.search_project, name='search'),
    ]
