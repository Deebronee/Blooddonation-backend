import hmac
from base64 import b64encode
from hashlib import sha256
import os
from django.http import HttpResponseForbidden
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
        secret = os.environ.get('API_KEY')
        body = request.body.decode('utf-8') or ""
        data = secret + "-" + request.method + "-" + request.path + "-" + body
        dataBytes = data.encode('utf-8')
        computed_sig = hmac.new(
            secret.encode('utf-8'),
            msg=dataBytes, digestmod=sha256
        ).digest()

        signature = b64encode(computed_sig).decode()

        print("request.headers")
        print(request.headers)
        print("data")
        print(data)
        print("bytes")
        print(dataBytes)
        print("signature")
        print(signature)

        return signature == api_signature
