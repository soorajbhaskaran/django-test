from newapp import views
from django.urls import path

app_name = 'new_app'

urlpatterns = [path('index/',views.index, name='index'),
               path('registration/', views.register, name='register'),
               path('loginuser/', views.user_login, name='login')]
