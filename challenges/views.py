from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def index(request):
    return HttpResponse("Bienvenido")

def monthly_challenge(request, month): 
    if month=='january':
        return HttpResponse("Walk for at least 30 min every day.")
    elif month=='february':
        return HttpResponse("Go to the gym every day.")
    elif month=='march':
        return HttpResponse("Shower every day.")
    elif month=='april':
        return HttpResponse("Play soccer every day.")
    elif month=='may':
        return HttpResponse("Hang out with friends.")
    elif month=='june':
        return HttpResponse("Attend to school every day.")
    elif month=='july':
        return HttpResponse("Sleep at least 8 hours every day.")
    elif month=='august':
        return HttpResponse("Enjoy vacations.")
    elif month=='september':
        return HttpResponse("Finish all my tasks before the due date.")
    elif month=='october':
        return HttpResponse("Enjoy the time with my family every day.")
    elif month=='november':
        return HttpResponse("Start a personal project.")
    elif month=='december':
        return HttpResponse("Celebrate Christmas and New Year.")
    else:
        return HttpResponseNotFound("Month not found")


def dictionary(request, month):
    diccionario={
        "january":"Walk for at least 30 min every day.",
        "february":"Go to the gym every day.",
        "march":"Shower every day.",
        "april":"Play soccer every day.",
        "may":"Hang out with friends.",
        "june":"Attend to school every day.",
        "july":"Sleep at least 8 hours every day.",
        "august":"Enjoy vacations.",
        "september":"Finish all my tasks before the due date.",
        "october":"Enjoy the time with my family every day.",
        "november":"Start a personal project.",
        "december":"Celebrate Christmas and New Year."
    } 
    
    
    
    

# TAREA
'''
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
'''