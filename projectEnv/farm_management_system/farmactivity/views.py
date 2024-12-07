from django.shortcuts import render , redirect
from .models import FarmActivity
from django.core.paginator import Paginator
from .forms import FarmActivityForm


# create farm_activity
def farm_activity(request):
    if request.method == 'POST':
        form = FarmActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('farm_activity_list')
    else:
        form = FarmActivityForm()
    return render(request,'farmactivity/farm_activity_form.html',{'form':form})    
# Read your family activity here.
def farm_activity_list(request):
    activity_list = FarmActivity.objects.all()
    paginator = Paginator(activity_list,5)
    page_number = request.GET.get('page')
    activities = paginator.get_page(page_number)
    return render(request,'farmactivity/farm_activity_list.html',{'activities':activities})


# update a single farm_activity

def update_farm_activity(request , pk):
     activity = FarmActivity.objects.get(pk=pk)
     if request.method == 'POST':
         form = FarmActivityForm(request.POST,instance=activity)
         if form.is_valid():
             form.save()
             return redirect('farm_activity_list')
     else:
         form=FarmActivityForm(instance=activity)
     return render(request,'farmactivity/farm_activity_form.html',{'form':form})        

# delete farm activity
 

def delete_farm_activity(request , pk):
    activity = FarmActivity.objects.get(pk=pk)
    if request.method == 'POST':
        activity.delete()
        return redirect('farm_activity_list')
    return render(request , 'farmactivity/farm_activity_delete.html',{'activity':activity})



    
    

    
    
