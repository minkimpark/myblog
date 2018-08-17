from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from backend.models import *
from django.utils import timezone

def upload_main(request):
    return render(request,'upload/upload_main.html')

def upload_write(request):
    return render(request,'upload/upload_write.html')

def api_upload_write_create(request):

    for f in request.FILES.getlist('myfile'): #myfile is the name of your html file button
        fname = f.name


    object = upload.objects.create(
        subject = request.POST['subject'],
        fname = str(fname),
    )
    return render(request,'upload/upload_main.html')
