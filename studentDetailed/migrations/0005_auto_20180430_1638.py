# Generated by Django 2.0.2 on 2018-04-30 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentDetailed', '0004_auto_20180430_0718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetailed',
            name='cgpa',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
    ]