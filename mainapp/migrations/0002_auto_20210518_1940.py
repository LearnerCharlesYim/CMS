# Generated by Django 2.2 on 2021-05-18 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cofextension',
            name='other',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='cofextension',
            name='remark',
            field=models.CharField(max_length=254, null=True),
        ),
    ]
