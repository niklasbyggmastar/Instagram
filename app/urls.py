from django.urls import path
from . import views

urlpatterns = [
    path('/', views.index, name='index'),
    path('user/<int:user_id>/', views.profile, name='profile'),
    path('post/<int:post_id>/', views.display_post, name='display_post'),
    path('explore/', views.explore, name='explore'),
    #----------Toiminnot-----------
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('init_profile/', views.init_profile, name='init_profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('post_view/', views.post_view, name='post_view'),
    path('follow/<int:user_id>/', views.follow, name='follow'),
    path('like/<int:post_id>/', views.like, name='like'),
    #path(r'^unlike/(?P<post_id>[0-9]+)/$', views.unlike, name='unlike'),
    path('post_comment/<int:post_id>/', views.post_comment, name='post_comment'),

]
