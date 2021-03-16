from django.db import models
from django.utils import timezone
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class CustomManager(models.Manager):
    def get_query(self):
        return super().get_query().filter(status='post')

class Video(models.Model):
    STATUS_CHOICES=(('draft','draft'),('post','Post'))
    video=models.FileField(null=True,blank=True,upload_to='videos/')
    image=models.ImageField(null=True,blank=True,upload_to='images/')
    title=models.CharField(max_length=400)
    slug=models.SlugField(max_length=400,unique_for_date='publish')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    publish=models.DateTimeField(default=timezone.now)
    uploaded=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    tags=TaggableManager()
    objects=CustomManager()

    class Meta:
        ordering=['-uploaded']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('videodetail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])

class Comment(models.Model):
    video=models.ForeignKey(Video,related_name='comments',on_delete=models.CASCADE)
    user=models.ForeignKey(User,related_name='users',on_delete=models.CASCADE)
    comment=models.TextField()
    commented=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    class Meta:
        ordering=['-commented']

    def __str__(self):
        return '{} commented'.format(str(self.user))

    def get_absolute_url(self):
        return reverse('comment',kwargs={'pk':slf.pk})

class Profile(models.Model):
    GENDER_CHOICES=(('male','Male'),('female','Female'),('other','Other'))
    username=models.ForeignKey(User,related_name='profile_users',on_delete=models.CASCADE)
    firstname=models.SlugField(max_length=24)
    email=models.EmailField()
    profilepic=models.ImageField(null=True,blank=True,upload_to='images/')
    birthday=models.DateField()
    bio=models.TextField()
    gender=models.CharField(max_length=10,choices=GENDER_CHOICES)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-created']

    def __str__(self):
        return str(self.username)
