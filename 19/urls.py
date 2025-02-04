from django.urls import path
from signup import views

app_name = 'signup'

urlpatterns = [
    # /signup
    path('', views.signup_form, name='signup_form'),
]