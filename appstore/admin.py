from django.contrib import admin
from models import AppFactory, UserInfo, TransactionDetails

class AppFactoryAdmin(admin.ModelAdmin):
    fields = ('title', 'text', 'appType','clickUrl', 'dummyUrl', 'bigImg','homeImg','dcrptnImg','optnlImg1','optnlImg2','optnlImg3','isBigBanner')
    list_display = ('title', 'clickUrl', 'dummyUrl', 'isBigBanner')    

class UserInfoAdmin(admin.ModelAdmin):
    fields = ('name', 'mobile', 'email', 'app')
    list_display = ('name', 'mobile', 'email', 'app')
    
class TransactionAdmin(admin.ModelAdmin):
    fields = ('user', 'amount', 'transactionNo', 'dateOfTransaction', 'onlResponse')
    list_display = ('user', 'amount', 'transactionNo', 'dateOfTransaction', 'onlResponse')
        
admin.site.register(AppFactory, AppFactoryAdmin)
admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(TransactionDetails, TransactionAdmin)   

