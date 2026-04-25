from django.shortcuts import render
from django.conf import settings
from django.core.cache import cache


class UnderConstructionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if settings.DEBUG and not request.path.startswith("/api/"):
            return render(request, "errors/under_construction.html", status=503)
        return self.get_response(request)


class AdminRatelimitMiddleware:
    MAX_ATTEMPTS = 5
    LOCKOUT_SECONDS = 300  # 5 menit lockout setelah 5x salah

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.path.startswith('/panel/'):
            return self.get_response(request)

        ip = self._get_ip(request)
        cache_key = f'admin_fail_{ip}'
        attempts = cache.get(cache_key, 0)

        if attempts >= self.MAX_ATTEMPTS:
            return render(request, 'errors/500.html', status=429)

        response = self.get_response(request)

        if request.method == 'POST' and '/panel/login/' in request.path:
            if response.status_code == 200:
                # Login gagal — tambah counter
                cache.set(cache_key, attempts + 1, self.LOCKOUT_SECONDS)
            else:
                # Login berhasil — reset counter
                cache.delete(cache_key)

        return response

    def _get_ip(self, request):
        forwarded = request.META.get('HTTP_X_FORWARDED_FOR')
        if forwarded:
            return forwarded.split(',')[0].strip()
        return request.META.get('REMOTE_ADDR', '')