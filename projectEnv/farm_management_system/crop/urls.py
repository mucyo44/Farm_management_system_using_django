from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.crop_list, name='crop_list'),
    path('<pk>/',views.crop_detail , name='crop_detail'),
    path('create/', views.crop_create , name='crop_create'),
    path('<pk>/update/', views.update_crop , name='crop_update'),
    path('<pk>/delete/',views.delete_crop,name='crop_delete')

]