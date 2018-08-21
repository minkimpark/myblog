from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from backend.models import *
from django.utils import timezone
from django.db import connections


def memo_main(request):
    object2 = memo.objects.all()
    return render(request,'memo/memo.html',object2)

def api_memo_create(request):
    object = memo.objects.create(
        comment = request.POST['comment'],
        writedate=timezone.now()
    )

    object2 = memo.objects.all()
    print(object2)

    return JsonResponse({'result':object2})
