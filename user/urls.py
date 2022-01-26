from django.urls import path
from . import views



####################################################################################
#########sign_up_view가 sign-up 경로를 통해서 작동을 하고 html을 통해서 보여준다.##############
####################################################################################
urlpatterns = [
    path('sign-up/', views.sign_up_view, name='sign-up'),
    path('sign-in/', views.sign_in_view, name='sign-in'),
    path('logout/', views.logout, name='logout'),
    path('user/', views.user_view,name='user-list'),
    path('user/follow/<int:id>',views.user_follow, name='user-follow'),

]