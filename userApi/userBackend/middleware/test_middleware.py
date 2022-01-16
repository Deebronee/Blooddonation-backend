from django.http import HttpResponseForbidden
import os
class TestMiddelware:

    def __init__(self, get_response):
        self.get_response = get_response

    
    def __call__(self, request):
        token = request.headers._store['authorization'][1]
        if token == os.environ.get('API_KEY'):
            response = self.get_response(request)
            return response
        else:
            return HttpResponseForbidden()
