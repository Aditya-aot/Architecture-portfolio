from django.db import models
from django.contrib.auth.models import User , auth 

# Create your models here.


class portfolio_models(models.Model) :
    title      = models.CharField(max_length=255 , null =True)
    top_portfolio  = models.BooleanField(default=False)
    author     =models.CharField(max_length=50 , null =True)
    position   =models.CharField(max_length=50 , null =True)
    author_detail =models.CharField(max_length=50 , null =True)
    time_start = models.DateField()
    time_end   = models.DateField()
    link       = models.CharField(max_length=255 , null =True)
    author_image = models.ImageField(upload_to='images/portfolio/author_img', blank=True, null=True)
    image      = models.ImageField(upload_to='images/portfolio/portfolio_main_img', blank=True, null=True)
    image2     = models.ImageField(upload_to='images/portfolio/portfolio_2img', blank=True, null=True)
    image3     = models.ImageField(upload_to='images/portfolio/portfolio_3img', blank=True, null=True)
    image4     = models.ImageField(upload_to='images/portfolio/portfolio_4img', blank=True, null=True)
    image5     = models.ImageField(upload_to='images/portfolio/portfolio_5img', blank=True, null=True)
    paragraph1 = models.CharField(max_length=255 , null =True)
    paragraph2 = models.CharField(max_length=255 , null =True)
    paragraph3 = models.CharField(max_length=255 , null =True)
    paragraph4 = models.CharField(max_length=255 , null =True)
    paragraph5 = models.CharField(max_length=255 , null =True)
    paragraph6 = models.CharField(max_length=255 , null =True)

class blogs_models(models.Model) :
    title     = models.CharField(max_length=255 , null =True)
    top_blog  = models.BooleanField(default=False)
    author    =models.CharField(max_length=50 , null =True)
    position  =models.CharField(max_length=50 , null =True)
    author_detail =models.CharField(max_length=50 , null =True)
    author_image = models.ImageField(upload_to='images/blog/author_img', blank=True, null=True)
    image     = models.ImageField(upload_to='images/blog/blog_main_img', blank=True, null=True)
    image2    = models.ImageField(upload_to='images/blog/blog_2img', blank=True, null=True)
    image3    = models.ImageField(upload_to='images/blog/blog_3img', blank=True, null=True)
    paragraph1 = models.CharField(max_length=255 , null =True)
    paragraph2 = models.CharField(max_length=255 , null =True)
    paragraph3 = models.CharField(max_length=255 , null =True)
    paragraph4 = models.CharField(max_length=255 , null =True)
    paragraph5 = models.CharField(max_length=255 , null =True)
    paragraph6 = models.CharField(max_length=255 , null =True)
    
    # def __str__(self) :
    #     return self.name