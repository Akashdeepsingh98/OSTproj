from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Welcome to polls app!")

def detail(request,question_id):
    return HttpResponse("You are looking at question %s."%question_id)

def results(request,question_id):
    return HttpResponse("You are looking at results of %s."%question_id)

def vote(request,question_id):
    return HttpResponse("You voted for question %s."%question_id)