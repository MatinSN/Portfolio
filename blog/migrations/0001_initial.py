# Generated by Django 2.0.13 on 2021-02-01 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_data', models.DateField(auto_created=True, auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('body', models.CharField(max_length=1000)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
