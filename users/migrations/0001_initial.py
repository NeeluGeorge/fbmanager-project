# Generated by Django 3.1.4 on 2020-12-12 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('fb_id', models.CharField(max_length=100)),
                ('fb_token', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Facebook User',
                'verbose_name_plural': 'Facebook Users',
            },
        ),
    ]
