from django.urls import path
from rest_framework import routers

from dvadmin.project.views import AppViewSet, AppGroupViewSet, DomainViewSet

project_url = routers.SimpleRouter()
project_url.register(r'app', AppViewSet)
project_url.register(r'appgroup', AppGroupViewSet)
project_url.register(r'domain', DomainViewSet)

urlpatterns = [
]
urlpatterns += project_url.urls
