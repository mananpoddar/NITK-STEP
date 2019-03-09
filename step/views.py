# from django.http import HttpResponse,HttpResponseRedirect
# from django.urls import reverse
# import datetime
# from django import template
# from django.utils import timezone
# from django.urls import reverse
from django.shortcuts import render
from .models import govtProjects, ongoingProgrammes, comingEvents


def frontPage(request):
    return render(request, "step/front-page.html")


def gov_projects(request):
    obj = govtProjects.objects.all()
    context = {'obj': obj}
    return render(request, 'step/info.html', context)


def ongoing(request):
    obj = ongoingProgrammes.objects.all()
    context = {'obj': obj}
    return render(request, 'step/info.html', context)


def comingevents(request):
    obj = comingEvents.objects.all()
    context = {'obj': obj}
    return render(request, 'step/info.html', context)


