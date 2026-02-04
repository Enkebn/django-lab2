from django.http import HttpResponse

def blog_home(request):
    return HttpResponse("This is Blog App page")
