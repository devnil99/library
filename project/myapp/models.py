from django.db import models

# Create your models here.
class AdminRegister(models.Model):
    username = models.CharField(max_length=20,blank=True)
    password = models.IntegerField(blank=True)
    
    def __str__(self):
        return self.username
    

class UserRegister(models.Model):
    username = models.CharField(max_length=20,blank=True)
    password = models.IntegerField(blank=True)
    
    def __str__(self):
        return self.username
    

class Book(models.Model):
    img = models.ImageField(upload_to='Book_Img',blank=True,null=True)
    book = models.CharField(max_length=20,blank=True)
    Auther = models.CharField(max_length=20,blank=True)



class BookRecord(models.Model):
    book = models.CharField(max_length=20,blank=True)
    date = models.DateField(auto_now=True,blank=True)
    apply = models.IntegerField(blank=True,null=True)
    issue = models.IntegerField(blank=True,null=True)

    
    def __str__(self):
        return self.username