from django.urls import path
from . import views


urlpatterns = [ 
    path('' ,views.livestock_list, name='livestock_list'),
    path('create/',views.create_livestock,name='livestock_create'),
    path('<int:pk>/update',views.update_livestock,name='update_livestock'),
    path('<int:pk>/delete',views.delete_livestock,name='delete_livestock')

]
