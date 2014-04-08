from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.template.loader import *
from coredirectory.directory.models import *

def home(request):
    c = {}
    return render_to_response('home.html', c)
