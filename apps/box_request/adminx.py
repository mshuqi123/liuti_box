import xadmin
# from xadmin.models import ArticleDetail
from xadmin import views
from xadmin.models import UserWidget
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side, Field
from box_request.models import Requests,Response,Param,Http_connect,Api_path,Get_time
from django.utils.safestring import mark_safe
# Register your models here.
class BaseSetting(object):
    enable_themes = True     #开启主题选择
    use_bootswatch = True
# 全局设置，最好放到adminx.py开头位置
class GlobalSettings(object):
    site_title = "测试管理平台"         # title内容
    site_footer = "流体网络-闪电盒子-测试组"            # 底部@后面
    menu_style = "accordion"      # 菜单折叠
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

class RequestsAdmin(object):
    list_display = ['name','state','host', 'path','hosta','hostd','paths','hosty', '参数','create_time','update_time']
    search_fields = ['name','hostd','update_time']  # 搜索栏
    list_filter = ['state','paths']  # 过滤器
    list_per_page = 10
    model_icon = 'fa fa-bell'
    filter_horizontal = ('query',)
    def 参数(self, obj):
        return [x.query for x in obj.query.all()]

class ResponseAdmin(object):
    list_display = ['fname','state','old', 'new','create_time','update_time']
    search_fields = ['fname','old']  # 搜索栏
    list_filter = ['state','new']  # 过滤器
    list_per_page = 10
    model_icon = 'fa fa-certificate'

class ParamAdmin(object):
    list_display = ['query', 'value','create_time','update_time']
    search_fields = ['query','update_time']  # 搜索栏
    list_filter = ['query']  # 过滤器
    list_per_page = 10
    model_icon = 'fa fa-github'

class Http_connectAdmin(object):
    list_display = ['yname','state','hosts', 'host','path','create_time','update_time']
    search_fields = ['yname','host','update_time']  # 搜索栏
    list_filter = ['state','path']  # 过滤器
    list_per_page = 10
    model_icon = 'fa fa-unlock'
class API_pathAdmin(object):
    list_display = ['name','id','path','state','update_time']
    search_fields = ['id','name','path','state']  # 搜索栏
    list_filter = ['state']  # 过滤器
    list_per_page = 10
    model_icon = 'fa fa-hdd-o'
class GET_timeAdmin(object):
    list_display = ['name','path','xtime','get_time']
    search_fields = ['name','path','get_time']  # 搜索栏
    list_filter = ['name','path','get_time']  # 过滤器
    list_per_page = 10
    model_icon = 'fa fa-bullhorn'

xadmin.site.register(Requests,RequestsAdmin)
xadmin.site.register(Response,ResponseAdmin)
xadmin.site.register(Param,ParamAdmin)
xadmin.site.register(Http_connect,Http_connectAdmin)
xadmin.site.register(Api_path,API_pathAdmin)
xadmin.site.register(Get_time,GET_timeAdmin)
