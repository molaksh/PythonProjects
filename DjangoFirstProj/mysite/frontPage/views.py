# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    #return HttpResponse("First Page\nFirst Page\nFirst Page\nFirst Page\nFirst Page\nFirst Page\nFirst Page\nFirst Page\n")
    return render(request, 'frontPage/frontPage.html', {})

# Create your views here.
