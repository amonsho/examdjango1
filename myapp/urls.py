from django.urls import path
from .views import home,get_user,add_user,update_user,delete_user,details_user,get_video,add_video,update_video,delete_video,details_video,user_videos,base,video_exclude_user

urlpatterns = [
    path('home/',home,name='home'),
    path('get_u/',get_user,name='get_u'),
    path('add_u/',add_user,name='add_u'),
    path('update_u/<int:id>',update_user,name='update_u'),
    path('delete_u/<int:id>',delete_user,name='delete_u'),
    path('details_u/<int:id>',details_user,name='details_u'),
    path('get_v/',get_video,name='get_v'),
    path('add_v/',add_video,name='add_v'),
    path('update_v/<int:id>',update_video,name='update_v'),
    path('delete_v/<int:id>',delete_video,name='delete_v'),
    path('details_v/<int:id>',details_video,name='details_v'),
    path('user/<int:user_id>/',user_videos, name='user_videos'),
    path('base/',base,name='base'),
    path('video/exclude/<int:user_id>',video_exclude_user,name='video_exclude_users')

]