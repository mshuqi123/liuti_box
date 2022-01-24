from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
from apps.tasks import add, mul

def task_demo(request):
    res = add.delay(10, 20)
    print(res.task_id)  # 返回task_id
    return JsonResponse({"code": 0, "res": res.task_id})
