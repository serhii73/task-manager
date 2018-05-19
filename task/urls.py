from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.to_login_redirect, name='to_login_redirect'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^create_task/$', views.create_task, name='createTask'),
    url(r'^all_tasks/$', views.all_task, name='all_task'),
    url(r'^task/(?P<pk>\d+)/$', views.task_detail, name='task_detail'),
    url(r'^validate_data/$', views.validate_data_form, name='validate_data'),
]
