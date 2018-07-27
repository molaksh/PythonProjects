# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
 
from django.http import HttpResponse

def index(request):
    #return HttpResponse("Welcome to Landing Page")
    return render(request, 'landingPage/landingPage.html', {})

# Create your views here.
