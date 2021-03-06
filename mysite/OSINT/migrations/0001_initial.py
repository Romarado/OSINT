# Generated by Django 3.2.4 on 2021-06-22 12:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('RequestID', models.BigAutoField(primary_key=True, serialize=False)),
                ('URL', models.CharField(max_length=100)),
                ('DateCreate', models.DateField(auto_now=True)),
                ('Place', models.CharField(blank=True, max_length=50)),
                ('FamilyInfo', models.CharField(blank=True, max_length=50)),
                ('Interests', models.CharField(blank=True, max_length=255)),
                ('Сharacter', models.CharField(blank=True, max_length=255)),
                ('AddedPersonality', models.CharField(blank=True, max_length=255)),
                ('GeoData', models.CharField(blank=True, max_length=100)),
                ('Photos', models.ImageField(blank=True, upload_to='')),
                ('Work', models.CharField(blank=True, max_length=255)),
                ('AddedDInfo', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('nickname', models.CharField(max_length=15)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ResponsesByObject',
            fields=[
                ('UniqueID', models.BigAutoField(primary_key=True, serialize=False)),
                ('UserID', models.BigIntegerField()),
                ('URL', models.CharField(max_length=100)),
                ('Date', models.DateField(blank=True, null=True)),
                ('Place', models.CharField(blank=True, max_length=50)),
                ('FamilyInfo', models.CharField(blank=True, max_length=50)),
                ('Interests', models.CharField(blank=True, max_length=255)),
                ('Сharacter', models.CharField(blank=True, max_length=255)),
                ('AddedPersonality', models.CharField(blank=True, max_length=255)),
                ('GeoData', models.CharField(blank=True, max_length=100)),
                ('Photos', models.ImageField(blank=True, upload_to='')),
                ('Work', models.CharField(blank=True, max_length=255)),
                ('AddedDInfo', models.CharField(blank=True, max_length=255)),
                ('RequestID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OSINT.requests')),
            ],
        ),
        migrations.AddField(
            model_name='requests',
            name='UserID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
