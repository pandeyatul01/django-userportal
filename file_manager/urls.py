from django.urls import path
from django.contrib.auth import views as auth_views

from .views import upload_file, file_list,home,CreateUserView,logout_view, view_profile


urlpatterns = [
    path("",home,name="home"),
    path("register/",CreateUserView.as_view(),name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="login.html"),
        name="login",
    ),
    path(
        "logout/",
        logout_view,
        name="logout",
    ),


    path('upload/', upload_file, name='upload-files'),
    path('files/', file_list, name='files-list'),
    path('view_profile/', view_profile, name='view_profile'),
]
