from django.contrib import admin
from web.models.user import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)    #逗号一定不能删除！！  因为这里要传的是列表，如果去掉后就是一个元素了
