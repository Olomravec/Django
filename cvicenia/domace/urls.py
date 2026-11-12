from django.urls import path
from . import views

urlpatterns = [
	path('ulohy/', views.ulohy, name='ulohy'), 
    path('du2_vizitka/', views.vizitka, name='vizitka'),
]