from django.conf.urls import url
from . import views, wechat_view

urlpatterns = [
        url(r'^$', views.index),
        url(r'^login/?$', views.login_page),
        url(r'^login_action/?$', views.login, name='login_action'),
        url(r'^wechat', wechat_view.index),
        url(r'^regist/?$', views.regist_page),
        url(r'^regist_action/?$', views.regist, name='regist_action'),
        url(r'^(\d)+/wills/?$', views.wills, name='will_list'),
        url(r'^create/?$', views.will_create_page, name='create_will'),
        url(r'^create_action/?$', views.will_create, name='create_will_action'),
        url(r'^(\d)+/moment/create/?$', views.moment_create_page, name='create_moment'),
        url(r'^(\d)+/moment/create_action/?', views.moment_create, name='create_moment_action'),
        url(r'^(\d)+/moment/list/?', views.moments, name='moment_list'),
]
