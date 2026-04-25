from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.http import url_has_allowed_host_and_scheme
from .forms import LoginForm
from .models import User


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')

    form = LoginForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()

        # Superadmin hanya boleh login via /panel/
        if user.role == User.SUPERADMIN:
            form.add_error(None, 'Username atau password salah.')
            return render(request, 'accounts/login.html', {'form': form})

        login(request, user)

        next_url = request.GET.get('next', '')
        safe = (
            next_url
            and url_has_allowed_host_and_scheme(next_url, allowed_hosts={request.get_host()})
            and next_url.startswith('/')
            and ' ' not in next_url
        )
        if safe:
            return redirect(next_url)
        return redirect('/')

    return render(request, 'accounts/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('/login/')
