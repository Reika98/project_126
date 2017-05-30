from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^faqs/$', views.render_faqs, name='faqs'),
    url(r'^activities/$', views.render_activities, name='activities'),
    url(r'^venues/$', views.render_venues, name='venues'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^add-activity/$', views.add_activity_view, name='add_activity'),
    url(r'^edit-activity/(?P<activity>\d+)$', views.edit_activity_view, name='edit_activity'),
    url(r'^delete-activity/(?P<id>\d+)$', views.delete_activity_view, name='delete_activity'),
    url(r'^edit-profile/$', views.edit_profile_view, name='edit_profile'),
    url(r'^(?P<username>\w+)$', views.profile_view, name='profile')
]
