# Generated by Django 3.0.7 on 2021-02-16 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_image', models.ImageField(blank=True, default='img/abc.jpg', null=True, upload_to='')),
                ('short_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WebContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_us', models.TextField()),
                ('mission', models.TextField()),
                ('email1', models.TextField()),
                ('email2', models.TextField()),
                ('speciality_image', models.ImageField(blank=True, default='img/abc.jpg', null=True, upload_to='')),
            ],
        ),
    ]
