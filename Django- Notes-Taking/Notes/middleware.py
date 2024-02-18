from django.shortcuts import redirect
from django.urls import resolve

class RedirectIfNotFoundMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if response.status_code == 404:
            # If the response status code is 404 (not found), redirect to the homepage
            return redirect('homepage')

        return response
