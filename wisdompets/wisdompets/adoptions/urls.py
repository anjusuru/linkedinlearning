from django.urls import path, include
from adoptions import views

app_name = 'adoptions'

urlpatterns = [
    path('', views.home, name='home'),
    path('adoptions/<pet_id>/', views.pet_detail, name='pet_detail'),
]
