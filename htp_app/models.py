from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Tag(models.Model):
    name = models.CharField(max_length=256)


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256)


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.URLField(null=True)
    registration_date = models.DateField(auto_now=True)
    rating = models.IntegerField(null=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.account.save()


class Article(models.Model):
    title = models.CharField(max_length=512, blank=False)
    text = models.TextField(blank=False)
    slug = models.SlugField(max_length=512)
    datetime = models.DateTimeField(auto_now=True)
    views = models.IntegerField(null=True)
    author = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='author')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    tags = models.ManyToManyField(Tag)


class Comment(models.Model):
    text = models.TextField(blank=False)
    datetime = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

