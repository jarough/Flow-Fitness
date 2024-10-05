from django.urls import path
from . import views

'app/model_viewtype'
'gym/equipment_detail.html'

urlpatterns = [
    path('', views.EquipmentListView.as_view(), name="gym-home"),
    path('gym/create/', views.EquipmentCreateView.as_view(), name="gym-create"),
    path('gym/<int:pk>/', views.EquipmentDetailView.as_view(), name="gym-details"),
    path('gym/<int:pk>/update', views.EquipmentUpdateView.as_view(), name="gym-update"),
    path('about/', views.about, name="gym-about"),
]
