from django.conf.urls import patterns,include,url
from appsgr.views import *
from django.contrib.auth.views import login,logout

urlpatterns=[
    url(r'^$',home,name='home'),
    url(r'^requerimento/list$',requerimento_list,name='requerimento_list'),
    url(r'^requerimento/detail/(?P<pk>\d+)$',requerimento_detail,name='requerimento_detail'),
    url(r'^requerimento/new$', requerimento_new, name='requerimento_new'),
    url(r'^requerimento/update/(?P<pk>\d+)$',requerimento_update,name='requerimento_update'),
    url(r'^requerimento/delete/(?P<pk>\d+)$',requerimento_delete,name='requerimento_delete'),

    url(r'^login/', login, {'template_name': 'utils/login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page': 'login'}, name='logout'),
    url(r'^erro_permissao/$', erro_permissao, name='erro_permissao'),
]