from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from box_request.models import Requests,Response,Http_connect
from django.db import connection
from django.core import serializers
# Create your views here.

def get_request(request):
    data = {}
    param = {}
    results = Requests.objects.filter(state='Q').order_by("-update_time").values()
    query = Requests.objects.filter(state='Q').order_by("-update_time").first()
    if results:
        results1 = query.query.all().values()
        param['query'] = list(results1)
        data['code'] = 200
        data["data"] = list(results)[0]
        data["param"] = param
        return JsonResponse(data, safe=False,json_dumps_params={'ensure_ascii':False})
    else:
        return JsonResponse({'status': 10022, 'message': '请求错误，请重试！'})
def get_response(request):
    data = {}
    results = Response.objects.filter(state='Q').order_by("-update_time").values()
    if results:
        data['code'] = 200
        data["data"] = list(results)[0]
        return JsonResponse(data, safe=False,json_dumps_params={'ensure_ascii':False})
    else:
        return JsonResponse({'status': 10022, 'message': '请求错误，请重试！'})
def http_connect(request):
    data = {}
    results = Http_connect.objects.filter(state='Q').order_by("-update_time").values()
    if results:
        data['code'] = 200
        data["data"] = list(results)[0]
        return JsonResponse(data, safe=False,json_dumps_params={'ensure_ascii':False})
    else:
        return JsonResponse({'status': 10022, 'message': '请求错误，请重试！'})