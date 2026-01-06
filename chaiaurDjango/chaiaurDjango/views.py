from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("Hello, world. i am your god")
    return render(request, 'website/index.html')
    
def about(request):
    # return HttpResponse("Hello, world. i am your god, this is about page")
    return render (request, 'website/about.html')

def contact(request):
    return HttpResponse("Hello, world. i am your god, this is contact page")