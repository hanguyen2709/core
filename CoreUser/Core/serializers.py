from rest_framework import serializers
from .models import CoreUsers, UserLogs

class CoreUsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = CoreUsers
        fields = '__all__'


class UserLogsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserLogs
        fields = '__all__'
