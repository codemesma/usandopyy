
from django.db import models
from django.urls import reverse

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from hitcount.models import HitCountMixin
from hitcount.settings import MODEL_HITCOUNT


class Book(models.Model):
    title  = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    book_available = models.BooleanField(default=False)
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
