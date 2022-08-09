from django.urls import path
from . import views

app_name = 'user_app'

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register_req,name='register'),
    path('login/',views.login_req,name='login'),
    path('logout/',views.logout_req,name='logout'),
]
