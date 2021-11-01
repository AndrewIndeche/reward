from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns=[
        url(r'^$',views.index,name = 'index'),
        url(r'^profile/$',views.profile,name='profile'),
        url(r'^profile/edit_profile$', views.edit_profile, name='edit_profile'),
        url(r'^project/(\d+)/$', views.project, name='project'),
        url(r'^search/', views.search_project, name='search'),
        ]
