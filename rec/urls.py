from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home",views.home,name="home"),
    path("signup",views.signup,name="signup"),
    path("signin",views.signin,name="signin"),
    path("signout",views.signout,name="signout"),
    path("experience/add",views.addexperience,name="addexperience"),
    path("experience/filter/<str:id>",views.getExpList,name="experience"),
    path("experience/details/<int:id>",views.getExpDetails,name="experiencedetails")
]