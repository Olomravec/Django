from django.urls import path
from . import views

urlpatterns = [
	path('ulohy/', views.ulohy, name='ulohy'), 
]