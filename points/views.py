from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    ip = get_client_ip(request)
    # get a list of all points
    # group points by geofences
    return HttpResponse("Hello, world. You're at the points index.")

def test(request, lat, lon):
    return HttpResponse("You hit my endpoint with {} and {}" % (lat, lon))

# http://stackoverflow.com/questions/4581789/how-do-i-get-user-ip-address-in-django
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

