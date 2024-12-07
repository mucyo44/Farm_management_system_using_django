from django.shortcuts import render , redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from .forms import UserSignupForm , UserLoginForm
from crop.models import Crop
from records.models import Records
from farmactivity.models import  FarmActivity
from django.db.models import Sum
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request , 'farm/home.html')

def register(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
        messages.success(request, 'Your account has been created successfully!')
    else:                            
        form = UserSignupForm()
    return render(request,'farm/signup.html',{'form':form}) 


def user_login(request):
    if request.method == 'POST':
        form =UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('landingPage')  # Replace 'home' with your desired success URL
            else:
                return render(request, 'farm/login.html', {'form': form, 'error': 'Invalid credentials'})
        else:
            return render(request, 'farm/login.html', {'form': form, 'error': 'Form is not valid'})
    
    else:  # For GET requests, return the login form
        form = UserLoginForm()
        return render(request, 'farm/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')


def dashboard(request):
    # Calculate the total number of livestock
    total_livestock = Records.objects.count()

    # Sum up the yield amount for crops
    total_crops = Crop.objects.aggregate(Sum('yield_amount'))['yield_amount__sum'] or 0

    # Get the most recent activity (assuming Activity model with a 'date' field)
    recent_activity = FarmActivity.objects.order_by('-end_date').first()

    return render(request, 'farm/landingPage.html', {
        'total_livestock': total_livestock,
        'total_crops': total_crops,
        'recent_activity': recent_activity.name if recent_activity else "No recent activity"
    })


