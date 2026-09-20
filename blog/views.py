from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('personal blog')

def about(request):
    return HttpResponse('Я Тимур и я пиздабол')
