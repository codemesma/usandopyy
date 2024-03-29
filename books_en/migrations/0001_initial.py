# Generated by Django 3.1.4 on 2022-08-06 04:51

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=300, unique=True)),
                ('book_available', models.BooleanField(default=False)),
                ('web', models.URLField(blank=True, null=True, verbose_name='Web')),
                ('buy', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('image_url', models.ImageField(blank=True, null=True, upload_to='static/livros/uploads/%Y/%m/%d/')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('meta_description', models.TextField(blank=True, max_length=160, null=True)),
                ('keywords', models.TextField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Book_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.CharField(max_length=200, unique=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('meta_description', models.TextField(blank=True, max_length=160, null=True)),
                ('meta_keywords', models.TextField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(blank=True, max_length=200, null=True, on_delete=django.db.models.deletion.SET_NULL, to='books_en.book')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_category', to='books_en.book_category'),
        ),
    ]
