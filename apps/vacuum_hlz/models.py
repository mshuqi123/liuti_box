from django.db import models

# Create your models here.

class Bucket(models.Model):
    '''需求实验分桶'''
    value = models.CharField(max_length=100, verbose_name="分桶名称", primary_key=True, unique=True, default="")
    describe = models.CharField(max_length=1000, verbose_name="分桶策略描述", blank=True, null=True, default="")
    state_choices = (
        (u'J', u'禁用'),
        (u'Q', u'启用'),
    )
    state = models.CharField(max_length=10,
                             choices=state_choices,
                             verbose_name="状态",
                             default="Q")
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name="最后更新时间")
    class Meta:
        db_table = 'hlz_bucket'
        verbose_name = "分桶策略"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.value
class User_bucket(models.Model):
    '''用户分桶桶号'''
    uid = models.IntegerField(verbose_name="用户id", default="")
    value = models.CharField(max_length=100, verbose_name="分桶名称", default="")
    num = models.IntegerField(verbose_name="桶号", default="")
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name="最后更新时间")
    class Meta:
        db_table = 'hlz_user_bucket'
        verbose_name = "用户桶号"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.uid
class User_equipment(models.Model):
    '''用户设备id'''
    uid = models.IntegerField(verbose_name="用户id", default="")
    value = models.CharField(max_length=100, verbose_name="设备id", blank=True, null=True, default="")
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name="最后更新时间")
    class Meta:
        db_table = 'hlz_equipment'
        verbose_name = "设备信息"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.uid
class User(models.Model):
    '''用户信息表'''
    yid = models.IntegerField(verbose_name="用户yid", unique=True, default="")
    phone = models.IntegerField(verbose_name="手机号", unique=True, blank=True, null=True, default="")
    cash_balance = models.FloatField(verbose_name="现金余额", blank=True, null=True, default="")
    gold_coin_balance = models.FloatField(verbose_name="金币余额", blank=True, null=True, default="")
    tongdun_decision = models.CharField(max_length=100, verbose_name="同盾状态", blank=True, null=True, default="")
    user_name = models.CharField(max_length=100, verbose_name="用户姓名", blank=True, null=True, default="")
    num_id = models.IntegerField(verbose_name="身份证号", blank=True, null=True, default="")
    alipay = models.CharField(max_length=100, verbose_name="支付宝号", blank=True, null=True, default="")
    channel = models.CharField(max_length=100, verbose_name="渠道号", blank=True, null=True, default="")
    edition = models.CharField(max_length=100, verbose_name="注册版本号", blank=True, null=True, default="")
    wechat_open_id = models.CharField(max_length=100, verbose_name="微信openid", blank=True, null=True, default="")
    wechat_name = models.CharField(max_length=100, verbose_name="微信昵称", blank=True, null=True, default="")
    tourist = models.BooleanField(max_length=100, verbose_name="是否是游客", default="")
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    # 最后更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name="最后登陆时间")
    class Meta:
        db_table = 'hlz_user'
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.yid
