from django.contrib import admin
from models import AppFactory, UserInfo, TransactionDetails, Banner,\
    HomePageText

class AppFactoryAdmin(admin.ModelAdmin):
    fields = ('title', 'text', 'subtext','appType','clickUrl', 'dummyUrl','homeImg','dcrptnImg','optnlImg1','optnlImg2','optnlImg3')
    list_display = ('title', 'clickUrl', 'dummyUrl')    

class UserInfoAdmin(admin.ModelAdmin):
    fields = ('name', 'mobile', 'email', 'app')
    list_display = ('name', 'mobile', 'email', 'app')
    
class TransactionAdmin(admin.ModelAdmin):
    fields = ('user', 'amount', 'transactionNo', 'dateOfTransaction', 'onlResponse')
    list_display = ('user', 'amount', 'transactionNo', 'dateOfTransaction', 'onlResponse')

admin.site.register(HomePageText)
admin.site.register(Banner)        
admin.site.register(AppFactory, AppFactoryAdmin)
admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(TransactionDetails, TransactionAdmin)   

