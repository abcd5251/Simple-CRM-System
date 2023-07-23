from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),  # create home page
    # path('login/', views.login_user, name = "login"),  # create login page
    # path('logout/', views.logout_user, name = "logout"),  # create home page
]
