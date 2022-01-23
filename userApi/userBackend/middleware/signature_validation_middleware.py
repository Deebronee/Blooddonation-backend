import hmac
from base64 import b64encode
from hashlib import sha256
import os
import re
from django.http import HttpResponseForbidden
from django.conf import settings
class SignatureValidationMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    
    def __call__(self, request):
        if self.is_valid(request):
            response = self.get_response(request)
            return response
        else:
            return HttpResponseForbidden()
        
    def is_valid(self, request):
        api_signature = request.headers.get('Signature')
        secret = settings.SIGNATURE_SECRET
        body = request.body.decode('utf-8') or ""
        params = [
            secret, request.method,
            request.path, body
        ]
        data = "-".join(params)
        data = data.encode('utf-8')
        computed_sig = hmac.new(
            secret.encode('utf-8'),
            msg=data, digestmod=sha256
        ).digest()
        print(request.headers)
        print(data)
        signature = b64encode(computed_sig).decode()
        print(signature)
        return signature == api_signature
