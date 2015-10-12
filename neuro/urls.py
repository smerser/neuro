from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('main.views',
    url(r'^neuro/$', 	                     'login_page',  name='login'),
    url(r'^neuro/logout/$',                'logout_page', name='logout'),

    url(r'^neuro/all/$',                   'show_all',    name='show_all'),
    url(r'^neuro/all/(?P<all>.+)/$',       'show_all',    name='show_all'),
    url(r'^neuro/add/$',                   'add_one',     name='add_one'),
    url(r'^neuro/del/(?P<id>.+)/$',        'del_one',     name='del_one'),
    url(r'^neuro/one/(?P<id>.+)/$',        'show_one',    name='show_one'),
    url(r'^neuro/cpr/(?P<cpr>[0-9\-]+)/$', 'get_cpr',     name='get_cpr'),
    url(r'^neuro/rapporter/$',             'rapporter',   name='rapporter'),
    url(r'^neuro/rscript/$',               'rscript',     name='rscript'),
    
    url(r'^neuro/admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^neuro/user/password/reset/$',      									'password_reset', {'post_reset_redirect' : '/neuro/user/password/reset/done/'}, name="password_reset"),
    url(r'^neuro/user/password/reset/done/$',		    						'password_reset_done'),
    url(r'^neuro/user/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',	'password_reset_confirm', {'post_reset_redirect' : '/neuro/user/password/done/'}),
    url(r'^neuro/user/password/done/$',											'password_reset_complete'),
    url(r'^neuro/accounts/login/$', 'login'),
)
