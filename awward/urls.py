from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
        url(r'^$',views.index,name = 'index'),
        url(r'^accounts/register/complete/$', views.edit_profile, name='edit_profile'),
        url(r'^profile/$',views.profile,name='profile'),
        url(r'^profile/<user>/settings', views.edit_profile, name='edit'),
        url(r'^project/(\d+)/$', views.project, name='project'),
        url(r'^search/', views.search_project, name='search'),
        ]
