# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse("Polls Page\nPolls Page\nPolls Page\nPolls Page\nPolls Page\n")
    return render(request, 'polls/polls.html',{} )

# Create your views here.
