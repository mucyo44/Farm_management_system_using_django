from django.shortcuts import render  , redirect
from .models import Crop
from  .forms import CropForm
from django.core.paginator import Paginator


# create a new crop

def crop_create(request):
    if request.method == 'POST':
        form = CropForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crop_list')
    else:
        form = CropForm()
    return render(request ,'crop/crop_form.html' , {'form':form})

# Read all crops

def crop_list(request):
    crops = Crop.objects.all()
    paginator = Paginator(crops,5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'crop/crop_list.html', {'page_obj':page_obj})

#update crop

def update_crop(request,pk):
    crop = Crop.objects.get(id=pk)
    if request.method == 'POST':
        form = CropForm(request.POST,instance=crop)
        if form.is_valid():
            form.save()
            return redirect('crop_list')
    else:
        form=CropForm(instance=crop)
    return render(request , "crop/crop_form.html" , {'form':form})        

# Detail view for a single crop

def crop_detail(request,pk):
    crop = Crop.objects.get(id=pk)
    return render(request , 'crop/crop_detail.html' , {'crop':crop})

#delete crop

def delete_crop(request,pk):
    crop = Crop.objects.get(id=pk)
    if request.method =='POST' :
        crop.delete()
        return redirect('crop_list')
    return render(request , 'crop/crop_delete.html',{'crop':crop})




       

