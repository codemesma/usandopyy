# Generated by Django 3.1.4 on 2022-07-25 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_slug'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Download',
        ),
    ]