from django.shortcuts import render
from django.contrib import admin
from django.db import models
from django.conf import settings



def Breweries(request):
    return render(request, 'main/main.html') #passes the data in here.
        #  return UserProfile.objects.get(user=self.request.user)
