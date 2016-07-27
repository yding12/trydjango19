from django.conf.urls import url
from django.contrib import admin
from . import views
from .views import(
    post_detail,
    post_create,
    post_delete,
    post_update,
    post_list,
)

urlpatterns = [

    url(r'^$', post_list, name='list'),
    url(r'^(?P<id>\d+)/$', post_detail, name='detail'),
    url(r'^create/$', post_create),
    url(r'^(?P<id>\d+)/delete/$', post_delete),
    url(r'^(?P<id>\d+)/edit/$', post_update, name='update'),

]

# urlpatterns = [
#
#     url(r'^$', "posts.views.post_home"),
#     url(r'^create/$', "posts.views.post_create"),
#     url(r'^delete/$', "posts.views.post_delete"),
#     url(r'^update/$', "posts.views.post_update"),
#     url(r'^list/$', "posts.views.post_list"),
#     #url(r'^posts/$', "<appname>.view.<function_name>")
# ]
