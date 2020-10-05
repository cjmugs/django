from django.db.models import Max
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello There, This is a website!")

def chris(request):
    return HttpResponse("This is Chris I am talking to . . . I think?")

def max(request):
        return HttpResponse("No wait, it is max!")

def mel(request):
    return HttpResponse("Melanie is the Queen!")
# left off at23:22