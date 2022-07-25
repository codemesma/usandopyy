
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from hitcount.models import HitCountMixin
from hitcount.settings import MODEL_HITCOUNT



class Download(models.Model):
    nome = models.CharField(max_length=500)
    featured_image = models.ImageField(upload_to='static/categoria/uploads/%Y/%m/%d/', blank=True, null=True)
    slug = models.CharField(max_length=250, unique=True)
    description = RichTextUploadingField(blank=True, null=True, config_name='special', external_plugin_resources=[('youtube', '/static/ckeditor/ckeditor_plugins/youtube/', 'plugin.js',)],)
    web = models.URLField('Web', null=True, blank=True)
    meta_description = models.TextField(max_length=160, null=True, blank=True)
    keywords = models.TextField(max_length=500, blank=True)

    def get_absolute_url(self):
        kwargs = {

            'slug': self.slug
        }

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)
        super(Download, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome


class Book_Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    description = RichTextUploadingField(blank=True, null=True, config_name='special', external_plugin_resources=[('youtube', '/static/ckeditor/ckeditor_plugins/youtube/', 'plugin.js',)],)
    meta_description = models.TextField(max_length=160, null=True, blank=True)
    meta_keywords = models.TextField(max_length=255, null=True, blank=True)
    

    class Meta:
        ordering = ['-id']

    def get_absolute_url(self):
        kwargs = {

            'slug': self.slug
        }

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Book_Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Book(models.Model):
    title  = models.CharField(max_length = 200)
    category = models.ForeignKey(Book_Category, on_delete=models.CASCADE, related_name='book_category')
    author = models.CharField(max_length = 200)
    book_available = models.BooleanField(default=False)
    web = models.URLField('Web', null=True, blank=True)
    buy = RichTextUploadingField(blank=True, null=True, config_name='special', external_plugin_resources=[('youtube', '/static/ckeditor/ckeditor_plugins/youtube/', 'plugin.js',)],)
    description = RichTextUploadingField(blank=True, null=True, config_name='special', external_plugin_resources=[('youtube', '/static/ckeditor/ckeditor_plugins/youtube/', 'plugin.js',)],)
    price = models.FloatField(null=True, blank=True)
    image_url = models.ImageField(upload_to='static/livros/uploads/%Y/%m/%d/', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    meta_description = models.TextField(max_length=160, null=True, blank=True)
    keywords = models.TextField(max_length=500, blank=True)
    

    def __str__(self):
        return self.title


class Order(models.Model):
	product = models.ForeignKey(Book, max_length=200, null=True, blank=True, on_delete = models.SET_NULL)
	created =  models.DateTimeField(auto_now_add=True) 

	def __str__(self):
		return self.product.title
