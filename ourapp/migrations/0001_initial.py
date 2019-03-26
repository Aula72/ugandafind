# Generated by Django 2.0 on 2018-11-03 00:33

import ckeditor_uploader.fields
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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=400)),
                ('article_body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('article_type', models.CharField(blank=True, choices=[('P', 'political history'), ('H', 'healthy'), ('C', 'culture'), ('E', 'education'), ('R', 'religion'), ('I', 'economics'), ('A', 'agriculture'), ('S', 'sports and games'), ('G', 'geography'), ('T', 'tourism')], max_length=1, null=True)),
                ('article_references', models.CharField(blank=True, max_length=1000, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=1000)),
                ('image', models.FileField(default=None, upload_to='')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ourapp.Article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_text', models.CharField(max_length=9000)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ourapp.Article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
