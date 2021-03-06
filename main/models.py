import datetime
import os
from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from hitcount.models import HitCountMixin
from hitcount.settings import MODEL_HITCOUNT


ROLE_CHOICE = (
    ('Admin', 'Admin'),
    ('Publisher', 'Publisher'),
    ('Author', 'Author'),
)

STATUS_CHOICE = (
    ('Drafted', 'Drafted'),
    ('Published', 'Published'),
    ('Rejected', 'Rejected'),
    ('Trashed', 'Trashed'),
)

TUTORIAL_CHOICE = (
    ('Basico', 'Basico'),
    ('Avançado', 'Avançado'),
    ('Exercicios', 'Exercicios'),
)




class Download(models.Model):
    nome = models.CharField(max_length=500)
    featured_image = models.ImageField(upload_to='static/categoria/uploads/%Y/%m/%d/', blank=True, null=True)
    slug = models.CharField(max_length=250, unique=True)
    description = RichTextUploadingField(blank=True, null=True, config_name='special', external_plugin_resources=[('youtube', '/static/ckeditor/ckeditor_plugins/youtube/', 'plugin.js',)],)
    web = models.URLField('Web', null=True, blank=True)
    meta_description = models.TextField(max_length=160, null=True, blank=True)
    keywords = models.TextField(max_length=500, blank=True)

    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='Drafted')
    nivel = models.CharField(max_length=12, choices=TUTORIAL_CHOICE, default='Basico')

    def get_absolute_url(self):
        kwargs = {

            'slug': self.slug
        }

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)
        super(Download, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome


class Sobre(models.Model):
    nome = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to='images/profile', blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    enderesso = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=150, blank=True, null=True)
    web = models.URLField('Web', null=True, blank=True)
    youtube = models.URLField('youtube', null=True, blank=True)
    facebook = models.URLField('Facebook', null=True, blank=True)
    instagram = models.URLField('Instagram', null=True, blank=True)
    twiter = models.URLField('Twiter', null=True, blank=True)

    def __str__(self):
        return self.nome


class Author(models.Model):
    nome = models.CharField(max_length=255)
    imagem = models.ImageField(
        upload_to='images/profile', blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    enderesso = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=150, blank=True, null=True)
    web = models.URLField('Web', null=True, blank=True)
    youtube = models.URLField('youtube', null=True, blank=True)
    facebook = models.URLField('Facebook', null=True, blank=True)
    instagram = models.URLField('Instagram', null=True, blank=True)
    twiter = models.URLField('Twiter', null=True, blank=True)

    def __str__(self):
        return self.nome


class Tipo(models.Model):
    name = models.CharField(max_length=50, unique=True)
    icon = models.CharField(max_length=200, unique=False)

    featured_image = models.ImageField(
        upload_to='static/tipo/uploads/%Y/%m/%d/', blank=True, null=True)

    class Meta:
        ordering = ['-id']

    def get_absolute_url(self):
        kwargs = {

            'name': self.name
        }

    def __str__(self):
        return self.name

    def tipo(self):
        return Categoria.objects.filter(category=self).count()


class Categoria(models.Model):
    name = models.CharField(max_length=50, unique=True)
    featured_image = models.ImageField(
        upload_to='static/categoria/uploads/%Y/%m/%d/', blank=True, null=True)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    slug = models.CharField(max_length=200, unique=True)
    description = RichTextUploadingField(blank=True, null=True, config_name='special', external_plugin_resources=[
        ('youtube', '/static/ckeditor/ckeditor_plugins/youtube/', 'plugin.js',)],)
    is_active = models.BooleanField(default=False)
    meta_description = models.TextField(max_length=160, null=True, blank=True)
    meta_keywords = models.TextField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']

    def get_absolute_url(self):
        kwargs = {

            'slug': self.slug
        }

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Categoria, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def category_posts(self):
        return Tutorial.objects.filter(category=self).count()


class Tutorial(models.Model, HitCountMixin):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    meta_description = models.TextField(max_length=160, null=True, blank=True)
    user = models.ForeignKey(Author, on_delete=models.CASCADE)

    content = RichTextUploadingField(blank=True, null=True, config_name='special', external_plugin_resources=[
        ('youtube', '/static/ckeditor/ckeditor_plugins/youtube/', 'plugin.js',)],)
    category = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, related_name='category')
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICE, default='Drafted')
    nivel = models.CharField(
        max_length=12, choices=TUTORIAL_CHOICE, default='Basico')
    keywords = models.TextField(max_length=500, blank=True)
    featured_image = models.ImageField(
        upload_to='static/tutorial/uploads/%Y/%m/%d/', blank=True, null=True)

    class Meta:
        ordering = ['-category']

    def get_absolute_url(self):
        kwargs = {

            'slug': self.slug
        }
        return reverse('tutorial-view', kwargs=kwargs)

    def save(self, *args, **kwargs):
        tempslug = slugify(self.title)
        if self.id:
            blogpost = Tutorial.objects.get(pk=self.id)
            if blogpost.title != self.title:
                self.slug = create_slug(tempslug)
        else:
            self.slug = create_slug(tempslug)

        super(Tutorial, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def is_deletable_by(self, user):
        if self.user == user or user.is_superuser:
            return True
        return False

    def store_old_slug(self, old_slug):
        query = Post_Slugs.objects.filter(
            blog=self, slug=old_slug).values_list("slug", flat=True)
        if not (query and old_slug != self.slug):
            old_slug, _ = Post_Slugs.objects.get_or_create(
                blog=self, slug=old_slug)
            old_slug.is_active = False
            old_slug.save()
        active_slug, _ = Post_Slugs.objects.get_or_create(
            blog=self, slug=self.slug)
        active_slug.is_active = True
        active_slug.save()


def create_slug(tempslug):
    slugcount = 0
    while True:
        try:
            Tutorial.objects.get(slug=tempslug)
            slugcount += 1
            tempslug = tempslug + '-' + str(slugcount)
        except ObjectDoesNotExist:
            return tempslug


class Post_Slugs(models.Model):
    blog = models.ForeignKey(Tutorial, related_name='slugs',
                             on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.slug


class Image_File(models.Model):
    upload = models.FileField(upload_to="static/uploads/%Y/%m/%d/")
    date_created = models.DateTimeField(default=datetime.datetime.now)
    is_image = models.BooleanField(default=True)
    thumbnail = models.FileField(
        upload_to="static/uploads/%Y/%m/%d/", blank=True, null=True)

    def __str__(self):
        return self.date_created


class ContactUsSettings(models.Model):
    from_email = models.EmailField()
    reply_to_email = models.EmailField(blank=True, null=True)
    email_admin = models.EmailField()
    subject = models.CharField(max_length=500)
    body_user = models.TextField()
    body_admin = models.TextField()
