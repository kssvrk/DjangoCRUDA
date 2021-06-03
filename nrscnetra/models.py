from django.db import models
from django.conf import settings
#This is to store the models related to systems monitoring App NRSC Netra.
User=settings.AUTH_USER_MODEL
class System(models.Model):
    #title to register system as
    title = models.CharField(max_length = 200)
    #max length of ipv6=39
    ip_address= models.CharField(max_length=40,unique=True,blank=False,null=False)
    #registered_by_user
    added_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    system_id = models.AutoField(primary_key=True)

    def __str__(self):
        return f"{self.title}_{self.ip_address}"






