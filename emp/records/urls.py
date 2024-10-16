from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.data_list, name='data_list'),  # URL for listing data entries
    path('data/<int:data_id>/', views.data_detail, name='data_detail'),  # URL for specific data entry details
]
