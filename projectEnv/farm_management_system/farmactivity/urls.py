from django.urls import path
from . import views



urlpatterns = [ 
    path('',views.farm_activity_list,name='farm_activity_list'),
    path('create/',views.farm_activity,name='farm_activity_form'),
    path('<pk>/update/',views.update_farm_activity,name='update_farm_activity'),
    path('<pk>/delete',views.delete_farm_activity,name='farm_activity_delete')

]
