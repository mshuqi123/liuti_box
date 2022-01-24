import xadmin
# from xadmin.models import ArticleDetail
from xadmin import views
from xadmin.models import UserWidget
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side, Field
from vacuum_hlz.models import User, User_equipment, User_bucket, Bucket
from django.utils.safestring import mark_safe
# Register your models here.

class UserAdmin(object):
    list_display = ['id', 'yid', 'phone', 'cash_balance', 'gold_coin_balance', 'user_name', 'num_id', 'tourist', 'tongdun_decision', 'alipay', 'channel', 'edition', 'wechat_open_id', 'wechat_name', 'create_time', 'update_time']
    search_fields = ['id', 'yid', 'phone', 'alipay']  # 搜索栏
    list_filter = ['yid', 'phone', 'tourist']  # 过滤器
    list_per_page = 10
    model_icon = 'fa fa-unlink'

    def has_add_permission(self, request=None):
        # Disable delete
        return False

class User_equipmentAdmin(object):
    list_display = ['uid', 'value', 'create_time', 'update_time']
    search_fields = ['uid', 'value']  # 搜索栏
    list_filter = ['uid', 'value']  # 过滤器
    list_per_page = 10
    model_icon = 'fa fa-question'
    def has_add_permission(self, request=None):
        # Disable delete
        return False

class User_bucketAdmin(object):
    list_display = ['uid', 'value', 'num', 'create_time', 'update_time']
    search_fields = ['id', 'value']  # 搜索栏
    list_filter = ['id']  # 过滤器
    list_per_page = 10
    model_icon = 'fa fa-info'
    def has_add_permission(self, request=None):
        # Disable delete
        return False

class BucketAdmin(object):
    list_display = ['value', 'describe', 'state', 'create_time', 'update_time']
    search_fields = ['value']  # 搜索栏
    list_filter = ['value', 'state']  # 过滤器
    list_per_page = 10
    model_icon = 'fa fa-maxcdn'

xadmin.site.register(User, UserAdmin)
xadmin.site.register(User_equipment, User_equipmentAdmin)
xadmin.site.register(User_bucket, User_bucketAdmin)
xadmin.site.register(Bucket, BucketAdmin)
