from django.db import models
from django.conf import settings
#This is to store the models related to systems monitoring App NRSC Netra.
User=settings.AUTH_USER_MODEL
#------------------ SYSTEM MODEL----------------
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

#----------------------- JOBDEF MODEL-----------------
class JobDef(models.Model):
    jobdef_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200,unique=True,null=False,blank=False) #has to be in sync with the API of client
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"JOB Definition : {self.name}"
#------------------ JOB MODEL-----------------------
class Job(models.Model):
    job_id=models.AutoField(primary_key=True)
    type=models.ForeignKey(
        JobDef,
        on_delete=models.CASCADE
    )
    system=models.ForeignKey(
        System,
        on_delete=models.CASCADE
    )
    argument=models.CharField(max_length=500)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"JOB : {self.type}_{self.job_id}"





