from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from backend.models import *
from django.utils import timezone
from django.db import connections

def main(request):
    with connections['default'].cursor() as cur:
        query = '''
            select num,id,subject,writedate,hits
            from board;
        '''
        cur.execute(query)
        boards = cur.fetchall()
    context = {}
    context['boards'] = boards
    return render(request, 'main/main.html', context)

def write(request):
    return render(request,'main/write.html')

def api_write_create(request):

    object2 = board(
        id = request.POST['id'],
        subject = request.POST['subject'],
        content = request.POST['content'],
        writedate=timezone.now(),
        hits =0
    )
    object2.save()

    return JsonResponse({'result':'success'})

def api_write_read(request):
    num = request.GET['num']
    boardData = board.objects.get(num=num)
    board.objects.filter(num=num).update(hits = boardData.hits+1)
    boardData = board.objects.get(num=num)

    context = {}
    context['num'] = boardData.num
    context['id'] = boardData.id
    context['subject'] = boardData.subject
    context['content'] = boardData.content
    context['writedate'] = boardData.writedate
    context['hits']=boardData.hits
    print(context)
    return render(request,'main/view.html',context)

def modify(request):
    num = request.GET['num']
    boardData = board.objects.get(num=num)
    context = {}
    context['num'] = boardData.num
    context['id'] = boardData.id
    context['subject'] = boardData.subject
    context['content'] = boardData.content
    return render(request,'main/modify.html',context)


def api_write_update(request):
    boardData = board.objects.get(num=request.POST['num'])
    boardData.subject = request.POST['subject']
    boardData.content = request.POST['content']
    boardData.save()

    context = {}
    context['subject'] = boardData.subject
    context['content'] = boardData.content
    context['result'] = 'success'
    return JsonResponse({'result':context})

def api_write_delete(request):
    boardData = board.objects.get(num=request.POST['num'])
    boardData.delete()
    return JsonResponse({'result':'success'})
