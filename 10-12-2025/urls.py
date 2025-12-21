from django.urls import path
from .views import hello,check,status,get_request,put_request,del_request,post_request,api_view
from .views import api_view
urlpatterns = [
    path('hello/', hello),
    path('hello/check/',check),
    path('hello/status/',status),
    path('get_request/',get_request),
    path('put_request/',put_request),
    path('post_request/',post_request),
    path('put_request/',put_request),
    path('del_request/',del_request),
    path('api_view/',api_view),

