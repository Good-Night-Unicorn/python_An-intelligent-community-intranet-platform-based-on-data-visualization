#coding:utf-8
__author__ = "ila"
from django.db import models

from .model import BaseModel

from datetime import datetime



class zhuhu(BaseModel):
    __doc__ = u'''zhuhu'''
    __tablename__ = 'zhuhu'

    __loginUser__='zhuhuzhanghao'


    __authTables__={}
    __authPeople__='是'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __loginUserColumn__='zhuhuzhanghao'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    zhuhuzhanghao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='住户账号' )
    mima=models.CharField ( max_length=255,null=False, unique=False, verbose_name='密码' )
    zhuhuxingming=models.CharField ( max_length=255,null=False, unique=False, verbose_name='住户姓名' )
    xingbie=models.CharField ( max_length=255, null=True, unique=False, verbose_name='性别' )
    nianling=models.IntegerField  (  null=True, unique=False, verbose_name='年龄' )
    shouji=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机' )
    loudonghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='楼栋号' )
    zhuzhi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='住址' )
    shenfenzhenghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='身份证号' )
    fanzuiqianke=models.CharField ( max_length=255,null=False, unique=False, verbose_name='犯罪前科' )
    '''
    zhuhuzhanghao=VARCHAR
    mima=VARCHAR
    zhuhuxingming=VARCHAR
    xingbie=VARCHAR
    nianling=Integer
    shouji=VARCHAR
    loudonghao=VARCHAR
    zhuzhi=VARCHAR
    shenfenzhenghao=VARCHAR
    fanzuiqianke=VARCHAR
    '''
    class Meta:
        db_table = 'zhuhu'
        verbose_name = verbose_name_plural = '住户'
class laifangdengji(BaseModel):
    __doc__ = u'''laifangdengji'''
    __tablename__ = 'laifangdengji'



    __authTables__={'zhuhuzhanghao':'zhuhu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    laifangshijian=models.DateTimeField  (  null=True, unique=False, verbose_name='来访时间' )
    laifangrenyuan=models.CharField ( max_length=255, null=True, unique=False, verbose_name='来访人员' )
    shoujihaoma=models.CharField ( max_length=255, null=True, unique=False, verbose_name='手机号码' )
    zhuhuzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='住户账号' )
    zhuhuxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='住户姓名' )
    loudonghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='楼栋号' )
    tiwen=models.FloatField   (  null=True, unique=False, verbose_name='体温' )
    jinrushijian=models.DateTimeField  (  null=True, unique=False, verbose_name='进入时间' )
    chuqushijian=models.DateTimeField  (  null=True, unique=False, verbose_name='出去时间' )
    beizhu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='备注' )
    '''
    laifangshijian=DateTime
    laifangrenyuan=VARCHAR
    shoujihaoma=VARCHAR
    zhuhuzhanghao=VARCHAR
    zhuhuxingming=VARCHAR
    loudonghao=VARCHAR
    tiwen=Float
    jinrushijian=DateTime
    chuqushijian=DateTime
    beizhu=VARCHAR
    '''
    class Meta:
        db_table = 'laifangdengji'
        verbose_name = verbose_name_plural = '来访登记'
class churudengji(BaseModel):
    __doc__ = u'''churudengji'''
    __tablename__ = 'churudengji'



    __authTables__={'zhuhuzhanghao':'zhuhu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='是'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    dengjibianhao=models.CharField ( max_length=255,null=False,unique=True, verbose_name='登记编号' )
    zhuhuzhanghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='住户账号' )
    zhuhuxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='住户姓名' )
    leixing=models.CharField ( max_length=255, null=True, unique=False, verbose_name='类型' )
    dengjishijian=models.DateTimeField  (  null=True, unique=False, verbose_name='登记时间' )
    beizhu=models.CharField ( max_length=255, null=True, unique=False, verbose_name='备注' )
    '''
    dengjibianhao=VARCHAR
    zhuhuzhanghao=VARCHAR
    zhuhuxingming=VARCHAR
    leixing=VARCHAR
    dengjishijian=DateTime
    beizhu=VARCHAR
    '''
    class Meta:
        db_table = 'churudengji'
        verbose_name = verbose_name_plural = '出入登记'
class wuyecuijiao(BaseModel):
    __doc__ = u'''wuyecuijiao'''
    __tablename__ = 'wuyecuijiao'



    __authTables__={'zhuhuzhanghao':'zhuhu',}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    yuefen=models.CharField ( max_length=255,null=False, unique=False, verbose_name='月份' )
    zhuhuzhanghao=models.CharField ( max_length=255,null=False, unique=False, verbose_name='住户账号' )
    zhuhuxingming=models.CharField ( max_length=255, null=True, unique=False, verbose_name='住户姓名' )
    loudonghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='楼栋号' )
    zhuzhi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='住址' )
    jiaofeileixing=models.CharField ( max_length=255,null=False, unique=False, verbose_name='缴费类型' )
    feiyong=models.FloatField   (  null=True, unique=False, verbose_name='费用' )
    feiyongqingdan=models.TextField   (  null=True, unique=False, verbose_name='费用清单' )
    jiaofeishijian=models.DateTimeField  (  null=True, unique=False, verbose_name='缴费时间' )
    jiezhishijian=models.DateTimeField  (  null=True, unique=False, verbose_name='截止时间' )
    feiyongxiangqing=models.TextField   (  null=True, unique=False, verbose_name='费用详情' )
    ispay=models.CharField ( max_length=255, null=True, unique=False,default='未支付', verbose_name='是否支付' )
    '''
    yuefen=VARCHAR
    zhuhuzhanghao=VARCHAR
    zhuhuxingming=VARCHAR
    loudonghao=VARCHAR
    zhuzhi=VARCHAR
    jiaofeileixing=VARCHAR
    feiyong=Float
    feiyongqingdan=Text
    jiaofeishijian=DateTime
    jiezhishijian=DateTime
    feiyongxiangqing=Text
    ispay=VARCHAR
    '''
    class Meta:
        db_table = 'wuyecuijiao'
        verbose_name = verbose_name_plural = '物业催缴'
class gaoweiloudong(BaseModel):
    __doc__ = u'''gaoweiloudong'''
    __tablename__ = 'gaoweiloudong'



    __authTables__={}
    __authPeople__='否'#用户表，表属性loginUserColumn对应的值就是用户名字段，mima就是密码字段
    __sfsh__='否'#表sfsh(是否审核，”是”或”否”)字段和sfhf(审核回复)字段，后台列表(page)的操作中要多一个”审核”按钮，点击”审核”弹出一个页面，包含”是否审核”和”审核回复”，点击确定调用update接口，修改sfsh和sfhf两个字段。
    __authSeparate__='否'#后台列表权限
    __thumbsUp__='否'#表属性thumbsUp[是/否]，新增thumbsupnum赞和crazilynum踩字段
    __intelRecom__='否'#智能推荐功能(表属性：[intelRecom（是/否）],新增clicktime[前端不显示该字段]字段（调用info/detail接口的时候更新），按clicktime排序查询)
    __browseClick__='否'#表属性[browseClick:是/否]，点击字段（clicknum），调用info/detail接口的时候后端自动+1）、投票功能（表属性[vote:是/否]，投票字段（votenum）,调用vote接口后端votenum+1
    __foreEndListAuth__='否'#前台列表权限foreEndListAuth[是/否]；当foreEndListAuth=是，刷的表新增用户字段userid，前台list列表接口仅能查看自己的记录和add接口后台赋值userid的值
    __foreEndList__='否'#表属性[foreEndList]前台list:和后台默认的list列表页相似,只是摆在前台,否:指没有此页,是:表示有此页(不需要登陆即可查看),前要登:表示有此页且需要登陆后才能查看
    __isAdmin__='否'#表属性isAdmin=”是”,刷出来的用户表也是管理员，即page和list可以查看所有人的考试记录(同时应用于其他表)
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    gaoweizhuangtai=models.CharField ( max_length=255, null=True, unique=False, verbose_name='高危状态' )
    loudonghao=models.CharField ( max_length=255, null=True, unique=False, verbose_name='楼栋号' )
    wenxintishi=models.CharField ( max_length=255, null=True, unique=False, verbose_name='温馨提示' )
    '''
    gaoweizhuangtai=VARCHAR
    loudonghao=VARCHAR
    wenxintishi=VARCHAR
    '''
    class Meta:
        db_table = 'gaoweiloudong'
        verbose_name = verbose_name_plural = '高危楼栋'
class news(BaseModel):
    __doc__ = u'''news'''
    __tablename__ = 'news'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255,null=False, unique=False, verbose_name='标题' )
    introduction=models.TextField   (  null=True, unique=False, verbose_name='简介' )
    picture=models.TextField   ( null=False, unique=False, verbose_name='图片' )
    content=models.TextField   ( null=False, unique=False, verbose_name='内容' )
    '''
    title=VARCHAR
    introduction=Text
    picture=Text
    content=Text
    '''
    class Meta:
        db_table = 'news'
        verbose_name = verbose_name_plural = '社区公告'
class aboutus(BaseModel):
    __doc__ = u'''aboutus'''
    __tablename__ = 'aboutus'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255,null=False, unique=False, verbose_name='标题' )
    subtitle=models.CharField ( max_length=255, null=True, unique=False, verbose_name='副标题' )
    content=models.TextField   ( null=False, unique=False, verbose_name='内容' )
    picture1=models.TextField   (  null=True, unique=False, verbose_name='图片1' )
    picture2=models.TextField   (  null=True, unique=False, verbose_name='图片2' )
    picture3=models.TextField   (  null=True, unique=False, verbose_name='图片3' )
    '''
    title=VARCHAR
    subtitle=VARCHAR
    content=Text
    picture1=Text
    picture2=Text
    picture3=Text
    '''
    class Meta:
        db_table = 'aboutus'
        verbose_name = verbose_name_plural = '关于我们'
class systemintro(BaseModel):
    __doc__ = u'''systemintro'''
    __tablename__ = 'systemintro'



    __authTables__={}
    addtime = models.DateTimeField(auto_now_add=False, verbose_name=u'创建时间')
    title=models.CharField ( max_length=255,null=False, unique=False, verbose_name='标题' )
    subtitle=models.CharField ( max_length=255, null=True, unique=False, verbose_name='副标题' )
    content=models.TextField   ( null=False, unique=False, verbose_name='内容' )
    picture1=models.TextField   (  null=True, unique=False, verbose_name='图片1' )
    picture2=models.TextField   (  null=True, unique=False, verbose_name='图片2' )
    picture3=models.TextField   (  null=True, unique=False, verbose_name='图片3' )
    '''
    title=VARCHAR
    subtitle=VARCHAR
    content=Text
    picture1=Text
    picture2=Text
    picture3=Text
    '''
    class Meta:
        db_table = 'systemintro'
        verbose_name = verbose_name_plural = '关于我们'
