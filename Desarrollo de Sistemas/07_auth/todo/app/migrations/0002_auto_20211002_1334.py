# Generated by Django 3.1.4 on 2021-10-02 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='nacionalidad',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Nacionalidad'),
        ),
        migrations.AlterField(
            model_name='user',
            name='colegio',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Colegio'),
        ),
    ]
