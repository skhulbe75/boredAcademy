from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse(request, "Hello Worlld")
    return render(request, 'random_website/index.html')