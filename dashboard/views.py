from django.shortcuts import render, redirect
from django_ratelimit.decorators import ratelimit

@ratelimit(key='ip', rate='60/m', block=True)
def home(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    
    if request.user.is_superuser:
        return redirect('/panel/')
    
    return render(request, 'dashboard.html')