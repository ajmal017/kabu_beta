# Generated by Django 2.2.7 on 2020-08-15 12:54

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='COMPANY',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LABEL',
            fields=[
                ('label_id', models.IntegerField(primary_key=True, serialize=False)),
                ('label_name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TAG',
            fields=[
                ('tag_id', models.AutoField(primary_key=True, serialize=False)),
                ('tag_name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TAGKUBUN',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NEWS',
            fields=[
                ('news_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=200)),
                ('description', models.CharField(default='', max_length=10000)),
                ('detail_url', models.CharField(default='', max_length=500)),
                ('class_id', models.IntegerField(default=0)),
                ('del_flg', models.IntegerField(default=0)),
                ('checked_flg', models.IntegerField(default=0)),
                ('url', models.CharField(default='', max_length=200)),
                ('detail', models.CharField(default='', max_length=10000)),
                ('create_date', models.DateField(default=django.utils.timezone.now)),
                ('company', models.ManyToManyField(blank=True, to='backend.COMPANY')),
                ('label', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='backend.LABEL')),
                ('tag', models.ManyToManyField(blank=True, to='backend.TAG')),
            ],
        ),
    ]
