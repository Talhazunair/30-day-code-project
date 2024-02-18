from django.db import models
from datetime import datetime
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
# Create your models here.
class Tag(models.Model):
    caption=models.CharField(max_length=20)
    def __str__(self):
        return (f"{self.caption}")
    
class Author(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    email_id=models.EmailField()
    
    def __str__(self):
        return (f"{self.first_name+self.last_name}")
    
class Post(models.Model):
    title=models.CharField(max_length=255,unique=True)
    description=models.CharField(max_length=200,null=True)
    slug=models.SlugField(unique=True,blank=True)
    content=models.TextField()
    published_date=models.DateTimeField(default=datetime.now)
    featured_image=models.ImageField(upload_to='blog_images')
    author=models.ForeignKey(Author,on_delete=models.SET_NULL,related_name="posts",null=True,default="Talha")
    tags=models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.title
    def slug_generator(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.title)[:255]
            super().save(*args,**kwargs)