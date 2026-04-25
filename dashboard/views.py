from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django_ratelimit.decorators import ratelimit


@login_required
@ratelimit(key='user', rate='20/m', block=True)
def home(request):
    return render(request, 'dashboard.html')
