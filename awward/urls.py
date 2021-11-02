from django.conf.urls import url
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns=[
        url(r'^$',views.index,name = 'index'),
        url(r'^profile/$',views.profile,name='profile'),
        url(r'^profile/edit_profile/$', views.edit_profile, name='edit_profile'),
        path('<username>/profile', views.user_profile, name='userprofile'),
        path('project/<post>', views.project, name='project'),
        url(r'^search/',views.search_project, name='search'),
        ]
