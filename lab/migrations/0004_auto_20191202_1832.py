# Generated by Django 2.2.7 on 2019-12-02 23:02

from django.db import migrations, models
import lab.models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0003_auto_20191202_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='edad',
            field=models.IntegerField(max_length=2),
        ),
    ]
