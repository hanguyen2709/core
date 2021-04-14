
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
from .models import CoreUsers, UserLogs
from .serializers import CoreUsersSerializer, UserLogsSerializer

def home(request):
    return HttpResponse('My first view.')


class UserViewSet(viewsets.ViewSet):
    
    """
    This class has 5 methods which allow to
        - get all user (list),
        - create new user (create),
        - retrieve specific user base on id of user (retrieve)
        - update specific user base on id of user (update)
        - delete specific user base on id of user (update)

    """

    def list(self, request):
        '''
        get list of all users from db
        '''

        users = CoreUsers.objects.all()
        serializer = CoreUsersSerializer(users, many=True)
        return Response(serializer.data)

    def create(self, request): #/api/user
        '''
        crete new user
        '''

        serializer = CoreUsersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None): #/api/user/<str:id>
        '''
        retrieve user base on id
        '''

        user = CoreUsers.objects.get(user_id=pk)
        serializer = CoreUsersSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        '''
        update user base on id param
        '''

        user = CoreUsers.objects.get(user_id=pk)
        serializer = CoreUsersSerializer(instance=user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        '''
        delete user based on id
        '''

        user = CoreUsers.objects.get(user_id=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class LogsViewSet(viewsets.ViewSet):
    """
    This class has 5 methods which allow to
        - get all user log  (list),
        - create new log for user (create),
        - retrieve all log of specific user base on id of user (retrieve)
        - update specific log base on id of user (update)
        - delete specific log base on id of log (update)

    """

    def list(self, request): #/logs/user
        '''
        get all logs
        '''

        users = UserLogs.objects.all()
        serializer = UserLogsSerializer(users, many=True)
        return Response(serializer.data)

    def create(self, request): #/logs/user
        '''
        create new log
        '''
        serializer = UserLogsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # get list of logs from user id
    def retrieve(self, request, pk=None): #/logs/user/<str:id>
        '''
        get all log of specific user id
        '''

        user = UserLogs.objects.get(id=pk)
        user_log = UserLogs.objects.filter(user_id_log=user.id)
        serializer = UserLogsSerializer(user_log, many=True)
        return Response(serializer.data)

    #update by id of record
    def update(self, request, pk=None):
        '''
        update speicific log base on id
        '''

        log = UserLogs.objects.get(id=pk)
        serializer = UserLogsSerializer(instance=log, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    # delete by id of record
    def destroy(self, request, pk=None):
        '''
        delete speicific log based on id
        '''

        log = UserLogs.objects.get(id=pk)
        log.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
