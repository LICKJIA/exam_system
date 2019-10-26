from django.db import models
from manager.models import *
from teacher.models import *

# Create your models here.
class History(models.Model):
    student = models.ForeignKey(Student,verbose_name='stuid')
    paper = models.ForeignKey(Papers,verbose_name='papid')
    grade = models.DecimalField(max_digits=4,decimal_places=1,verbose_name='grade')
    status = models.BooleanField(default=False)
    submitime = models.DateTimeField(auto_now=True)

class topic(models.Model):
    history = models.ForeignKey(History, verbose_name='hisid')
    ques = models.ForeignKey(Quess)
    answers = models.CharField(max_length=10)

