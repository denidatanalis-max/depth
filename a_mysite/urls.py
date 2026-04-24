from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Django is working! 🎉")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
]

handler404 = 'core.views.custom_404'
handler500 = 'core.views.custom_500'