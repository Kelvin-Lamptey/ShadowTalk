from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from .models import Chat
from userprofiles.models import UserProfile
import random
from math import radians, cos, sin, asin, sqrt

# Create your views here.

def landing_page(request):
    if request.user.is_authenticated:
        return home(request)
    return render(request, 'home/landing.html')

@login_required
def home(request):
    # Get recent chats
    recent_chats = Chat.objects.filter(
        participants=request.user
    ).order_by('-updated_at')[:5]

    # Handle search
    search_query = request.GET.get('search', '')
    search_results = []
    if search_query:
        search_results = User.objects.filter(
            username__icontains=search_query
        ).exclude(id=request.user.id)[:10]

    context = {
        'recent_chats': recent_chats,
        'search_results': search_results,
    }
    return render(request, 'home/home.html', context)

@login_required
def matchmaker(request):
    filters = {
        'school': request.GET.get('school'),
        'gender': request.GET.get('gender'),
    }
    
    matches = UserProfile.objects.all()
    
    if filters['school']:
        matches = matches.filter(school__icontains=filters['school'])
    if filters['gender']:
        matches = matches.filter(gender=filters['gender'])
        
    matches = matches.exclude(user=request.user)[:10]
    
    return render(request, 'home/matchmaker.html', {'matches': matches})

@login_required
def random_users(request):
    users = list(User.objects.exclude(id=request.user.id))
    random_users = random.sample(users, min(5, len(users)))
    return render(request, 'home/random_users.html', {'users': random_users})

@login_required
def nearby_users(request):
    def calculate_distance(lat1, lon1, lat2, lon2):
        lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a))
        r = 6371  # Radius of earth in kilometers
        return c * r

    user_profile = request.user.userprofile
    if not (user_profile.latitude and user_profile.longitude):
        return render(request, 'home/nearby_users.html', 
                     {'error': 'Please update your location in your profile'})

    nearby_users = []
    for profile in UserProfile.objects.exclude(user=request.user):
        if profile.latitude and profile.longitude:
            distance = calculate_distance(
                user_profile.latitude, user_profile.longitude,
                profile.latitude, profile.longitude
            )
            if distance <= 50:  # Within 50km
                nearby_users.append({'user': profile.user, 'distance': round(distance, 2)})
    
    return render(request, 'home/nearby_users.html', {'nearby_users': nearby_users})

@login_required
def same_school(request):
    user_school = request.user.userprofile.school
    if not user_school:
        return render(request, 'home/same_school.html', 
                     {'error': 'Please update your school in your profile'})
    
    school_mates = UserProfile.objects.filter(
        school__iexact=user_school
    ).exclude(user=request.user)
    
    return render(request, 'home/same_school.html', {'school_mates': school_mates})
