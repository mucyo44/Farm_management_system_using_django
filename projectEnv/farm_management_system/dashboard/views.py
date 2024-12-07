# dashboard/views.py

import matplotlib.pyplot as plt
import io
import base64
from django.shortcuts import render
from crop.models import Crop
from records.models import Records
from django.db.models import Count
from django.db.models.functions import TruncMonth
from collections import defaultdict
from django.db.models import Q

def generate_chart(data, chart_type, title, xlabel=None, ylabel=None):
    plt.figure(figsize=(10, 6))
    if chart_type == 'bar':
        plt.bar(data.keys(), data.values())
        if xlabel:
            plt.xlabel(xlabel)
        if ylabel:
            plt.ylabel(ylabel)
    elif chart_type == 'pie':
        plt.pie(data.values(), labels=data.keys(), autopct='%1.1f%%', startangle=90)
    plt.title(title)
    
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    
    return base64.b64encode(image_png).decode('utf-8')

def dashboard(request):
    # Crop Yield by Season
    crops_by_season = Crop.objects.values('season').annotate(crop_yield=Count('id'))
    season_data = {crop['season']: crop['crop_yield'] for crop in crops_by_season}
    crop_yield_chart = generate_chart(season_data, 'pie', 'Crop Yield by Season')
    
    # Animal Health Status
    animal_health = Records.objects.aggregate(
        sick=Count('id', filter=Q(status='unhealthy')),
        healthy=Count('id', filter=Q(status='healthy'))
    )
    animal_health_chart = generate_chart(animal_health, 'pie', 'Animal Health Status')
    
    context = {
        "crop_yield_chart": crop_yield_chart,
        "animal_health_chart": animal_health_chart,
    }
    
    return render(request, 'dashboard/dashboard.html', context)