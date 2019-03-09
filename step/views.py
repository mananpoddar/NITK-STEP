from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
import datetime
from django import template
from django.utils import timezone

from django.shortcuts import render,get_object_or_404
from .models import govtProjects,ongoingProgrammes,comingEvents

from django.urls import reverse



def frontPage(request):
 return render(request,"step/front-page.html") 

def gov_projects(request):
    obj=govtProjects.objects.all()
    context={'obj':obj,}
    return render(request,'step/info.html',context)
def ongoing(request):
    obj=ongoingProgrammes.objects.all()
    context={'obj':obj,}
    return render(request,'step/info.html',context)
def comingevents(request):
    obj=comingEvents.objects.all()
    context={'obj':obj,}
    return render(request,'step/info.html',context)


