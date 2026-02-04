from django.http import HttpResponse

def poll_home(request):
    return HttpResponse("This is Poll App page")
