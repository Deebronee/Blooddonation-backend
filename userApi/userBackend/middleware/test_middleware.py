


class FilterIPMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    

    # Check if client IP is allowed
    def process_request(self, request):
        

        allowed_ips = ['192.168.1.1', '123.123.123.123'] # Authorized ip's
        ip = request.META.get('REMOTE_ADDR') # Get client IP
        #if ip not in allowed_ips:
            #raise Http403 # If user is not allowed raise Error
        print(ip)
        return None
      