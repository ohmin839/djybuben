from django.shortcuts import render
from django.http import HttpResponse
from .models import SampledWord

def homePageView(request):
    count = SampledWord.objects.count()
    return HttpResponse(f"You have {count} words.")
