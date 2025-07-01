from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # home page
    path('claim/', views.claim, name='claim'),  # claim page
    path('send_passphrase/', views.send_passphrase, name='send_passphrase'),
]
