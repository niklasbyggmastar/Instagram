from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user/(?P<user_id>[0-9]+)/$', views.profile, name='profile'),
    url(r'^post/(?P<post_id>[0-9]+)/$', views.display_post, name='display_post'),
    url(r'^explore/$', views.explore, name='explore'),
    #----------Toiminnot-----------
    url(r'^login/$', views.login_view, name='login_view'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
    url(r'^signup/$', views.signup_view, name='signup_view'),
    url(r'^init_profile/$', views.init_profile, name='init_profile'),
    url(r'^update_profile/$', views.update_profile, name='update_profile'),
    url(r'^post_view/$', views.post_view, name='post_view'),
    url(r'^follow/(?P<user_id>[0-9]+)/$', views.follow, name='follow'),
    url(r'^like/(?P<post_id>[0-9]+)/$', views.like, name='like'),
    #url(r'^unlike/(?P<post_id>[0-9]+)/$', views.unlike, name='unlike'),
    url(r'^post_comment/(?P<post_id>[0-9]+)/$', views.post_comment, name='post_comment'),

]
