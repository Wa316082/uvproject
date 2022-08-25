from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


#Notice model

class Notice(models.Model):
    title = models.CharField(max_length=200)
    details = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    
    
class Comment(models.Model):
    body = models.TextField()
    aothor = models.ForeignKey(User, related_name='comments', on_delete = models.CASCADE )
    notice = models.ForeignKey( Notice, on_delete= models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s - %s' %(self.body, self.aothor)
