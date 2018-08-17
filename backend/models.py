from django.db import models

class member(models.Model):
    num = models.AutoField(primary_key=True)
    id = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    joindate = models.DateField(null=True,blank=True)

    class Meta :
        db_table = 'member'


class board(models.Model):
    num =models.AutoField(primary_key=True)
    id=models.CharField(max_length=25)
    subject = models.CharField(max_length=100)
    content = models.CharField(max_length=20000)
    writedate = models.DateTimeField(auto_now_add=True, blank=True)
    modify_date = models.DateTimeField(auto_now=True, blank=True)
    hits= models.IntegerField()

    class Meta :
        db_table = 'board'

class upload(models.Model):
    num =models.AutoField(primary_key=True)
    subject = models.CharField(max_length=100)
    fname = models.ImageField(blank=True, upload_to="kmweb/%Y/%m/%d")

    class Meta :
        db_table = 'upload'
