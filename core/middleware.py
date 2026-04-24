from django.shortcuts import render
from django.conf import settings

class UnderConstructionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if settings.DEBUG and not request.path.startswith("/api/"):
            return render(request, "errors/under_construction.html", status=503)

        return self.get_response(request)