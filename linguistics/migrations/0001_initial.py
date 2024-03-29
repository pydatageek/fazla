# Generated by Django 3.1.1 on 2020-09-22 16:18

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
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateTimeField(editable=False, verbose_name='added date')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='updated date')),
                ('name', models.CharField(max_length=245, unique=True, verbose_name='name')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True, verbose_name='slug')),
                ('unique_code', models.CharField(blank=True, db_index=True, default='', max_length=9, unique=True, verbose_name='unique code')),
                ('short_content', models.TextField(blank=True, default='', help_text='you can give short information.', max_length=250, verbose_name='short content')),
                ('content', ckeditor.fields.RichTextField(blank=True, default='', verbose_name='content')),
                ('meta_title', models.CharField(db_index=True, max_length=245, unique=True, verbose_name='meta title')),
                ('meta_description', models.CharField(blank=True, default='', max_length=245, verbose_name='meta description')),
                ('publish_at', models.DateTimeField(blank=True, null=True, verbose_name='publish date')),
                ('unpublish_at', models.DateTimeField(blank=True, null=True, verbose_name='unpublish date')),
                ('is_published', models.BooleanField(default=False, editable=False, verbose_name='is published')),
                ('family_text', models.CharField(blank=True, default='', max_length=250, verbose_name='family')),
                ('native_name', models.CharField(blank=True, default='', max_length=250, verbose_name='native name')),
                ('code', models.CharField(db_index=True, max_length=3, unique=True, verbose_name='code')),
                ('iso2', models.CharField(blank=True, max_length=2, null=True, verbose_name='ISO2')),
                ('iso3', models.CharField(blank=True, max_length=3, null=True, verbose_name='ISO3')),
                ('_639_2_b', models.CharField(blank=True, max_length=5, null=True, verbose_name='639-2/B')),
                ('_639_3', models.CharField(blank=True, max_length=100, null=True, verbose_name='639-3')),
                ('notes', models.TextField(blank=True, default='', verbose_name='notes')),
                ('added_by', models.ForeignKey(blank=True, default=None, help_text='User who added the db record.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='linguistics_language_adders', to=settings.AUTH_USER_MODEL, verbose_name='added by')),
                ('updated_by', models.ForeignKey(blank=True, default=None, help_text='User who updated the db record.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='linguistics_language_modifiers', to=settings.AUTH_USER_MODEL, verbose_name='updated by')),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
            },
        ),
        migrations.CreateModel(
            name='Alphabet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_at', models.DateTimeField(editable=False, verbose_name='added date')),
                ('updated_at', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='updated date')),
                ('name', models.CharField(max_length=245, unique=True, verbose_name='name')),
                ('slug', models.SlugField(blank=True, max_length=255, unique=True, verbose_name='slug')),
                ('unique_code', models.CharField(blank=True, db_index=True, default='', max_length=9, unique=True, verbose_name='unique code')),
                ('code', models.CharField(blank=True, default='', max_length=250, verbose_name='code')),
                ('short_content', models.TextField(blank=True, default='', help_text='you can give short information.', max_length=250, verbose_name='short content')),
                ('content', ckeditor.fields.RichTextField(blank=True, default='', verbose_name='content')),
                ('meta_title', models.CharField(db_index=True, max_length=245, unique=True, verbose_name='meta title')),
                ('meta_description', models.CharField(blank=True, default='', max_length=245, verbose_name='meta description')),
                ('publish_at', models.DateTimeField(blank=True, null=True, verbose_name='publish date')),
                ('unpublish_at', models.DateTimeField(blank=True, null=True, verbose_name='unpublish date')),
                ('is_published', models.BooleanField(default=False, editable=False, verbose_name='is published')),
                ('added_by', models.ForeignKey(blank=True, default=None, help_text='User who added the db record.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='linguistics_alphabet_adders', to=settings.AUTH_USER_MODEL, verbose_name='added by')),
                ('updated_by', models.ForeignKey(blank=True, default=None, help_text='User who updated the db record.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='linguistics_alphabet_modifiers', to=settings.AUTH_USER_MODEL, verbose_name='updated by')),
            ],
            options={
                'verbose_name': 'Alphabet',
                'verbose_name_plural': 'Alphabets',
            },
        ),
    ]
