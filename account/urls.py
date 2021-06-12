from django.urls import include, path
from . import views

app_name = 'account'

urlpatterns = [
    path('register/', views.account_register, name='register'),
    path('activate/<slug:uidb64>/<slug:token>/', views.account_activate, name='activate'),
    # User's Dashboard link
    path('dashboard/', views.dashboard, name='dashboard'),
]