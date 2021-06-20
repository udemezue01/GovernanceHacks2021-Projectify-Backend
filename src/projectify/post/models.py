from django.db import models
from django.conf import settings

# Create your models here.

class Post(models.Model):
    user        =   models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    text        =   models.CharField(max_length=3000, blank = True)
    file        =   models.FileField(blank = True)


    def __str__(self):
        return f'{self.user.full_name} - Post'




class Comment(models.Model):

    user          =   models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    target        =   models.ForeignKey(Post, on_delete = models.CASCADE)
    
    text           =  models.CharField(max_length=3000, blank=True)

    def __str__(self):

        return f'{self.user.full_name} -  Comment'