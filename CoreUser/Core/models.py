from django.db import models

# Create your models here.

class CoreUsers(models.Model):
    first_name = models.CharField(max_length = 10)
    last_name = models.CharField(max_length =10)
    user_id = models.IntegerField(primary_key=True)

    class Meta():
        verbose_name_plural = "Users"
        # fields = ['__all__']

    def __str__(self):
        return self.first_name

class UserLogs(models.Model):
    user_id_log = models.ForeignKey(CoreUsers, on_delete=models.CASCADE,)
    actions = models.CharField(max_length=50)
    service = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name_plural = "Logs"
        get_latest_by = "created_at"
        # fields = ('user_id_log','actions','service','created_at')

    def __str__(self):
        return '%s %s %s' % (self.user_id_log , self.actions ,  self.service)