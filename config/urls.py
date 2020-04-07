from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from eTutor import views as etutor_views
from django.conf.urls import url



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', etutor_views.homePage, name="homepage"),
    path('accounts/', include('registration.backends.simple.urls')),
    path('users/', etutor_views.usersPage, name="all_users"),
    path('rooms/', etutor_views.public_rooms, name="all_rooms"),
    path('my_dms/', etutor_views.my_dms),
    path('rooms/<slug:slug>', etutor_views.room_detail),
    path('rooms/<slug:slug>/dm_users/', etutor_views.dm_users),
    path('videoChat/', etutor_views.video_chat, name="video_chat"),
    url(r'token$', etutor_views.token, name="token"),
    path('direct_message/<slug:slug>', etutor_views.direct_message),
    path('edit/', etutor_views.user_edit, name="user_edit"),
    path('users/friend_request', etutor_views.friend_request),
    path('users/like/<int:pk>', etutor_views.like, name="like"),
    path('users/dislike/<int:pk>', etutor_views.dislike, name="dislike"),
    path('my_friends/', etutor_views.my_friends),
    path('friend_requests/', etutor_views.friend_requests),
    path('notification/get/', etutor_views.get_notifications),
    path('friend_requests/mark_read', etutor_views.mark_read),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
