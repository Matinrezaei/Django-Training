# Generated by Django 4.0.6 on 2022-08-04 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('First_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=264, unique=True)),
            ],
        ),
    ]
