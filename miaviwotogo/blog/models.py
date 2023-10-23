from email.policy import default
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from .helpers import *
from meta.models import ModelMeta
from ckeditor.fields import RichTextField


from ckeditor_uploader.fields import RichTextUploadingField


class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    website = models.URLField(max_length=200, blank=True)
    bio = models.CharField(max_length=1000, blank=True)
    token = models.CharField(max_length=100)
    image = models.ImageField(default="profile2.png", null=True, blank=True, upload_to='profil_pic')
    

    def __str__(self):
        return self.user.get_username()



class Categorie(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('accueil')


class Article(ModelMeta, models.Model):

    

    class Meta:
        ordering = ["-publish_date"]
        get_latest_by = "publish_date"

    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    contenu = RichTextUploadingField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog', blank=True, null=True)
    is_draft = models.BooleanField(default=True)
    user = models.ForeignKey(User, blank=True , null=True , on_delete=models.CASCADE)
    domaine = models.CharField(max_length=50)


    def __str__(self):
        return self.title

    @property
    def get_hit_count(self):
        return HitCount.objects.filter(article=self).count()

    def save(self , *args, **kwargs): 
        self.slug = generate_slug(self.title)
        super(Article, self).save(*args, **kwargs)


class HitCount(models.Model):

    ip_address = models.GenericIPAddressField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.ip_address} => {self.article.title}'
