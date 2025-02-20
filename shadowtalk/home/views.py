from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def landing_page(request):
    if request.user.is_authenticated:
        return render(request, 'home/dashboard.html')
    return render(request, 'home/landing.html')
