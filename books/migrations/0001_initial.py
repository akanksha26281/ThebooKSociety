# Generated by Django 3.2.5 on 2022-06-09 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('auther', models.CharField(max_length=125)),
                ('mode', models.CharField(default='public', max_length=11)),
                ('tag', models.CharField(max_length=75)),
                ('book_cover', models.ImageField(blank=True, upload_to='media/book_covers')),
                ('description', models.CharField(blank=True, max_length=500)),
            ],
        ),
    ]
