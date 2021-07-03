from django.urls import path

from . import views

urlpatterns = [
    path('',views.IndexView, name = 'index'),
    path('machine/',views.MachineListView, name = 'machine_list'),
    path('machine/<int:machine_id>/',views.MachineDetailView, name = 'machine_detail'),



    
]
