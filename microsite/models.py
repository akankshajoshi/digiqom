from django.db import models


class UserInfo(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    email = models.EmailField()
    join_date = models.DateTimeField(auto_now=True)
    ip_address = models.IPAddressField(null=True)
    
    def __unicode__(self):
        return self.name