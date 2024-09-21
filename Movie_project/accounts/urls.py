# accounts/urls.py
from django.urls import path 
from . import views 

#app name
app_name = 'accounts'

urlpatterns = [ 
    path('signup/', views.signup_view, name='signup'), # path for signup
    path('login/', views.login_view, name='login'), # path for login
    path('logout/', views.logout_view, name='logout') # path for logout
]