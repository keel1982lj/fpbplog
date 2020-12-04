from django.urls import path
from . import views

app_name = 'sdupass'

urlpatterns = [
    path('out/', views.go_out, name='out'),
    path('in/', views.go_in, name='in'),
]