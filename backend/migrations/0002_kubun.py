# Generated by Django 2.2.7 on 2020-08-15 12:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
                ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TAGKUBUN',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
            ],
        ),

    ]