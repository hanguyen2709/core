from django.contrib import admin
from .models import CoreUsers, UserLogs
# Register your models here.


class CoreUsersAdmin(admin.ModelAdmin):
    list_display = ( 'user_id','last_name','first_name' )
admin.site.register(CoreUsers,CoreUsersAdmin)


class LogsAdmin(admin.ModelAdmin):
    list_display = ('user_id_log_id','user_id_log','actions','service','created_at',)
admin.site.register(UserLogs,LogsAdmin)