# Generated by Django 3.2.4 on 2021-08-04 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kliniks', '0002_poli'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poli',
            name='nama',
            field=models.CharField(max_length=40),
        ),
    ]
