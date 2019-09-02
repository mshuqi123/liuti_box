from django.conf.urls import url
from apps.box_request import views
app_name = 'box_request'
urlpatterns = [
    url(r'^request$', views.get_request, name='request'),    # 异常请求
    url(r'^response$', views.get_response, name='response'),    # 异常返回
    url(r'^http_connect$', views.http_connect, name='response'),  # 整体异常返回
]
