from django.urls import path
from .views import UserViewSet, LogsViewSet


urlpatterns = [
    path('users', UserViewSet.as_view({
        'get':'list',
        'post':'create'
    })),
    path('users/<str:pk>', UserViewSet.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy',
    })),
    path('logs', LogsViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('logs/<str:pk>', LogsViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    })),
]
