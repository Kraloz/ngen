# Generated by Django 2.1.2 on 2018-11-10 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planta',
            name='extra',
            field=models.TextField(blank=True, null=True),
        ),
    ]
