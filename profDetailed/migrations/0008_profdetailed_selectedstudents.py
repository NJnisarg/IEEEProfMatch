# Generated by Django 2.0.2 on 2018-07-25 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profDetailed', '0007_remove_profdetailed_selectedstudents'),
    ]

    operations = [
        migrations.AddField(
            model_name='profdetailed',
            name='selectedStudents',
            field=models.TextField(blank=True, null=True),
        ),
    ]
