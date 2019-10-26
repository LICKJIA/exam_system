from django.db import models
from manager.models import *
# Create your models here.
class  Quess(models.Model):
    ques=models.TextField()
    choise1=models.TextField()
    choise2 = models.TextField()
    choise3 = models.TextField()
    choise4 = models.TextField()
    answer = models.CharField(max_length=10)
    explain = models.TextField()
    subid = models.ForeignKey(Subjs)
    createdate=models.DateField(auto_now_add=True)

class Papers(models.Model):
    quess=models.ManyToManyField(Quess)
    title=models.CharField(max_length=64)
    createtime=models.DateField(auto_now_add=True)
    subid=models.ForeignKey(Subjs)
    number=models.IntegerField(default=20)

class Testinf(models.Model):
    paper = models.OneToOneField(Papers)
    classmsg = models.ForeignKey(Classmsg)
    startime=models.DateTimeField()
    duration = models.IntegerField()
    deadline = models.DateTimeField()
    status = models.BooleanField()



