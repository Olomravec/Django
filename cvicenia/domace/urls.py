from django.urls import path
from . import views

urlpatterns = [
	path('ulohy/', views.ulohy, name='ulohy'), 
    path('du2_vizitka/', views.vizitka, name='vizitka'),
    path('teplota/', views.du3_teplota, name = "du3_teplota"),
]