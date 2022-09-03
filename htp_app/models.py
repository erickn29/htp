from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from pytils.translit import slugify
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(null=True)

    class Meta:
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.URLField(null=True)
    registration_date = models.DateField(auto_now=True)
    rating = models.IntegerField(null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.account.save()


class Article(models.Model):
    title = models.CharField(max_length=512, blank=False)
    text = RichTextUploadingField()
    poster = RichTextUploadingField()
    slug = models.SlugField(max_length=512, null=True, blank=True)
    datetime = models.DateTimeField(auto_now=True)
    views = models.IntegerField(null=True, blank=True)
    author = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='author')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    tags = models.ManyToManyField(Tag, null=True, blank=True, related_name='Tags')

    class Meta:
        verbose_name_plural = 'Статьи'

    def get_url(self):
        return reverse('article', args=[self.category__slug, self.slug])

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)


class Comment(models.Model):
    text = models.TextField(blank=False)
    datetime = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Account, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Комменты'

    def __str__(self):
        return self.author

