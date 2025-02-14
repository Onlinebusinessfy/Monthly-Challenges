from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request): 
    return HttpResponse("Este es un mensaje desde el index.")

def january(request):
    return HttpResponse("Walk for at least 30 min every day.")

def february(request):
    return HttpResponse("Go to the gym every day.")

def march(request):
    return HttpResponse("Shower every day.")

def april(request):
    return HttpResponse("Play soccer every day.")

def may(request):
    return HttpResponse("Hang out with friends.")

def june(request):
    return HttpResponse("Attend to school every day.")

def july(request):
    return HttpResponse("Sleep at least 8 hours every day.")

def august(request):
    return HttpResponse("Enjoy vacations.")

def september(request):
    return HttpResponse("Finish all my tasks before the due date.")

def october(request):
    return HttpResponse("Enjoy the time with my family every day.")

def november(request):
    return HttpResponse("Start a personal project.")

def december(request):
    return HttpResponse("Celebrate Christmas and New Year.")