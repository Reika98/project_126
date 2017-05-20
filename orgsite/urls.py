from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^faqs/$', views.render_faqs, name='faqs'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^profile/(?P<username>\w+)$', views.profile_view, name='profile')
]
