from django.urls import path
from . import views
urlpatterns = [
	path('cv1_index/', views.cv1_index, name = "cv1_index"),
    path('cv1_obchod/', views.cv1_obchod, name = "cv1_obchod"),
    path('cv1_body/', views.cv1_body, name = "cv1_body"),
]