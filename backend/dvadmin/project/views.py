# -*- coding: utf-8 -*-

"""
@author: H0nGzA1
@contact: QQ:2505811377
@Remark: 视图管理
"""

from dvadmin.project.models import App, AppGroup, Domain
from dvadmin.project.serializers import AppSerializer, AppGroupSerializer, DomainSerializer
from dvadmin.utils.viewset import CustomModelViewSet


class AppViewSet(CustomModelViewSet):
    """
    应用管理接口
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = App.objects.all()
    serializer_class = AppSerializer
    filter_fields = ['group']
    search_fields = ['name', 'use', 'host', 'bt_domain']


class AppGroupViewSet(CustomModelViewSet):
    """
    应用分组管理接口
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = AppGroup.objects.all()
    serializer_class = AppGroupSerializer
    filter_fields = ['name', 'id', 'parent']
    search_fields = ['name', 'key']


class DomainViewSet(CustomModelViewSet):
    """
    域名管理接口
    list:查询
    create:新增
    update:修改
    retrieve:单例
    destroy:删除
    """
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer
    filter_fields = ['group', 'type']
    search_fields = ['domain']
