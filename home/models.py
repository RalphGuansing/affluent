# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Schedule(models.Model):
    name = models.CharField(max_length=250)
    email_address = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=20)
    date_interview1 = models.CharField(max_length=250)
    date_interview2 = models.CharField(max_length=250)
    date_interview3 = models.CharField(max_length=250)
    start_internship = models.CharField(max_length=250)
    end_internship = models.CharField(max_length=250)


    def __str__(self):
        return self.name + ' - ' + self.email_address + ' - ' + self.contact_number




# class Applicant(models.Model):
    # applicant = models.ForeignKey(Schedule, on_delete=models.CASCADE)



