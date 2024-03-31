from django.urls import path
from django.contrib.auth.views import LoginView
from .forms import LoginForm

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='singup'),
    path('login/', LoginView.as_view(authentication_form=LoginForm, template_name='core/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout')
]