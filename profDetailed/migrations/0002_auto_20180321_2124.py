# Generated by Django 2.0.2 on 2018-03-21 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profDetailed', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profdetailed',
            name='areas',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='profdetailed',
            name='branch',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='profdetailed',
            name='keywords',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='profdetailed',
            name='minCgpa',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='profdetailed',
            name='minWorkEx',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='profdetailed',
            name='minYearOfStudy',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
