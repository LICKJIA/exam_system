from django.db import models

# Create your models here
class Classmsg(models.Model):
    classname=models.CharField(max_length=32,verbose_name='classname')
    regdate=models.DateField(auto_now_add=True)



class Student(models.Model):
    name = models.CharField(max_length=16)
    stuid = models.IntegerField(primary_key=True)
    classid = models.OneToOneField(Classmsg)
    school = models.CharField(max_length=32,blank=True)
    major = models.CharField(max_length=32,blank=True)
    email = models.EmailField(blank=True)
    regdate=models.DateTimeField(auto_now_add=True)
    possword=models.CharField(max_length=32)

class Teacher(models.Model):
    name = models.CharField(max_length=16)
    email=models.EmailField()
    regdate=models.DateTimeField(auto_now_add=True)
    possword = models.CharField(max_length=32)


class Subjs(models.Model):
    subname=models.CharField(max_length=32)

class Manager(models.Model):
    manager=models.CharField(max_length=32)
    premission=models.SmallIntegerField()
    possword = models.CharField(max_length=32)
    regdate=models.DateTimeField(auto_now_add=True)
