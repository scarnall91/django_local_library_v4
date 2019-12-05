from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resorts/', views.ResortListView.as_view(), name='resorts'),
    path('resort/<int:pk>', views.ResortDetailView.as_view(), name='resort-detail'),
    path('resorts/<int:pk>/update/', views.update_resort, name='update-resort'),
]
