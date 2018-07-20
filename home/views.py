# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from django.shortcuts import render
from .models import Schedule

def index(request):
    all_schedules = Schedule.objects.all()
    context = {'all_schedules' : all_schedules}
    return render(request, 'home/index.html', context)