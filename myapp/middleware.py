
from .models import IPAddress



class SaveIPAddressMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):

        # get ip
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        # check ip_address is in DB or not.
        try:
            ip_address = IPAddress.objects.get(ip_address=ip) # try to get ip in DB table
        except IPAddress.DoesNotExist:
            ip_address = IPAddress(ip_address=ip)
            ip_address.save() # save ip in DB
        request.user.ip_address = ip_address
        

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response