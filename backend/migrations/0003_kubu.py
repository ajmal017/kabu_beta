# Generated by Django 2.2.7 on 2020-08-15 12:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
         ('backend', '0002_kubun'),
    ]

    operations = [
        migrations.AddField(
                    model_name='TAG',
                    name='kubun_id',
                    field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.TAGKUBUN'),
                ),
    ]