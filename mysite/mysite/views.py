from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h1>Home page</h1>
        <ul>
            <li><a href="/poll/">Poll App</a></li>
            <li><a href="/blog/">Blog App</a></li>
        </ul>
    """)
from django.shortcuts import render

def home(request):
    return render(request, "index.html")

from django.http import HttpResponse

def home(request):
    return HttpResponse("Django Lab 2 - Amjilttai ajillaj baina")
