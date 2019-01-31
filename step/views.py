from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
import datetime
from django import template
from django.utils import timezone

from django.shortcuts import render,get_object_or_404

from django.urls import reverse



def frontPage(request):
 return render(request,"step/front-page.html") 

