from django.urls import path
from . import views

urlpatterns=[
  path('getapi/',views.ApiCall.as_view()),
  path('',views.home,name='home'),
  path('login/', views.login_view, name="login"),
]