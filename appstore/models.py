from django.db import models
# Create your models here.

class AppFactory(models.Model):
    title = models.CharField(max_length=250)
    subtext = models.TextField()
    text = models.TextField()
    clickUrl = models.URLField()
    dummyUrl = models.URLField(null=True,blank=True)
    homeImg = models.ImageField(upload_to='image/appstore/')
    dcrptnImg = models.ImageField(upload_to='image/appstore/')
    optnlImg1 = models.ImageField(upload_to='image/appstore/',null=True,blank=True)
    optnlImg2 = models.ImageField(upload_to='image/appstore/',null=True,blank=True)
    optnlImg3 = models.ImageField(upload_to='image/appstore/',null=True,blank=True)
    appType = models.IntegerField(choices=((1,'Web'),(2,'Mobile'),))
    createdDate = models.DateTimeField(auto_now=True)
    modifiedDate = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.title

class Banner(models.Model):
    image = models.ImageField(upload_to='image/banner/')
    createdDate = models.DateTimeField(auto_now_add=True)

class HomePageText(models.Model):
    text = models.TextField()
    
    def __unicode__(self):
        return self.text
 
class UserInfo(models.Model):
    name = models.CharField(max_length=250)
    mobile = models.CharField(max_length=12)
    email = models.EmailField()
    app = models.ForeignKey(AppFactory)
    
    def __unicode__(self):
        return self.name
    

class TransactionDetails(models.Model):
    user = models.OneToOneField(UserInfo)
    amount = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    transactionNo = models.IntegerField(null=True)
    dateOfTransaction = models.DateField(null=True)
    onlResponse  = models.CharField(max_length=10, blank=True, null=True) #online payment responses (Y : successful)(N : unsuccessful)(B : cant determine)(TO : timeout )
    
    
