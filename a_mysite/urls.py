from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('panel/', admin.site.urls),
    path('login/', lambda r: redirect('/accounts/login/', permanent=False)),
    path('logout/', lambda r: redirect('/accounts/logout/', permanent=False)),
    path('accounts/', include('accounts.urls')),
    path('', include('dashboard.urls')),
]

handler404 = 'core.views.custom_404'
handler500 = 'core.views.custom_500'
