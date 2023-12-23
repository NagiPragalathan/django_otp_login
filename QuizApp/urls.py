from django.contrib import admin
from django.urls import path, include
from base.views.auth import *
from base.views.common import *

urlpatterns = []

admin_ = [
    path('admin/', admin.site.urls),    
]

auth = [
    path('accounts/', include('django.contrib.auth.urls')),  # Use built-in authentication views
    path('enter_otp', enter_otp, name='enter_otp'),
    path('signup/<str:mail>', signup, name='signup'),
    path('login', user_login, name='login'),
]
common = [
    path('home', home, name='home'),
]

urlpatterns.extend(auth)
urlpatterns.extend(common)