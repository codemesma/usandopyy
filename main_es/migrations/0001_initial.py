# Generated by Django 3.1.4 on 2022-08-06 04:51

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion
import hitcount.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='images/profile')),
                ('descricao', models.TextField(blank=True, null=True)),
                ('enderesso', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=150, null=True)),
                ('web', models.URLField(blank=True, null=True, verbose_name='Web')),
                ('youtube', models.URLField(blank=True, null=True, verbose_name='youtube')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('twiter', models.URLField(blank=True, null=True, verbose_name='Twiter')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('featured_image', models.ImageField(blank=True, null=True, upload_to='static/categoria/uploads/%Y/%m/%d/')),
                ('slug', models.CharField(max_length=20, unique=True)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('meta_description', models.TextField(blank=True, max_length=160, null=True)),
                ('meta_keywords', models.TextField(blank=True, max_length=255, null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ContactUsSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_email', models.EmailField(max_length=254)),
                ('reply_to_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('email_admin', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=500)),
                ('body_user', models.TextField()),
                ('body_admin', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Image_File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(upload_to='static/uploads/%Y/%m/%d/')),
                ('date_created', models.DateTimeField(default=datetime.datetime.now)),
                ('is_image', models.BooleanField(default=True)),
                ('thumbnail', models.FileField(blank=True, null=True, upload_to='static/uploads/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Sobre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='images/profile')),
                ('descricao', models.TextField(blank=True, null=True)),
                ('enderesso', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=150, null=True)),
                ('web', models.URLField(blank=True, null=True, verbose_name='Web')),
                ('youtube', models.URLField(blank=True, null=True, verbose_name='youtube')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('twiter', models.URLField(blank=True, null=True, verbose_name='Twiter')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('icon', models.CharField(max_length=200)),
                ('featured_image', models.ImageField(blank=True, null=True, upload_to='static/tipo/uploads/%Y/%m/%d/')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateField(auto_now=True)),
                ('meta_description', models.TextField(blank=True, max_length=160, null=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Drafted', 'Drafted'), ('Published', 'Published'), ('Rejected', 'Rejected'), ('Trashed', 'Trashed')], default='Drafted', max_length=10)),
                ('nivel', models.CharField(choices=[('Basico', 'Basico'), ('Avançado', 'Avançado'), ('Exercicios', 'Exercicios')], default='Basico', max_length=12)),
                ('keywords', models.TextField(blank=True, max_length=500)),
                ('featured_image', models.ImageField(blank=True, null=True, upload_to='static/tutorial/uploads/%Y/%m/%d/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='main_es.categoria')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_es.author')),
            ],
            options={
                'ordering': ['-category'],
            },
            bases=(models.Model, hitcount.models.HitCountMixin),
        ),
        migrations.CreateModel(
            name='Post_Slugs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('is_active', models.BooleanField(default=False)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='slugs', to='main_es.tutorial')),
            ],
        ),
        migrations.AddField(
            model_name='categoria',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_es.tipo'),
        ),
        migrations.AddField(
            model_name='categoria',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_es.author'),
        ),
    ]
