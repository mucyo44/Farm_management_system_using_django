from django.shortcuts import render , redirect
from .models import Records
from django.core.paginator import Paginator
from .forms import LivestockForm



# Read livestock info
def livestock_list(request):

    livestock_list = Records.objects.all()
    paginator = Paginator(livestock_list,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'records/livestock_list.html',{'page_obj':page_obj})

# Create your views here.

def create_livestock(request):
    if request.method == 'POST' :
        form = LivestockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('livestock_list')
    else:
        form = LivestockForm()

    return render(request,'records/livestock_form.html',{'form':form})   


# update a single livestock

def update_livestock(request,pk):
    activity = Records.objects.get(pk=pk)
    if request.method == 'POST':
        form = LivestockForm(request.POST,instance=activity)
        if form.is_valid(): 
            form.save()

            return redirect('livestock_list')
    else:
        form = LivestockForm(instance=activity)
    return render(request,'records/livestock_form.html',{'form':form})   


#delete a single livestock

def delete_livestock(request, pk):
    activity = Records.objects.get(pk=pk)
    if request.method == 'POST':
        activity.delete()
        return redirect('livestock_detail')
    return render(request , 'records/livestock_delete.html', {'activity':activity})
