# Generated by Django 4.2.7 on 2023-11-16 19:37

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('summary', models.CharField(blank=True, max_length=150)),
                ('body', ckeditor.fields.RichTextField()),
                ('photo', models.ImageField(blank=True, upload_to='images/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('auther', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
