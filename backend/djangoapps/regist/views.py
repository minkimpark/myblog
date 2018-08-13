from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from backend.models import *
from django.utils import timezone

def regist(request):
    return render(request,'regist/regist.html')

def api_regist_create(request):


    data = member(
        id=request.POST.get('userid'),
        password=request.POST.get('userpwd'),
        name=request.POST.get('username'),
        email=request.POST.get('email'),
        joindate=timezone.now(),
    )
    data.save()

    return JsonResponse({'return':'success'})
