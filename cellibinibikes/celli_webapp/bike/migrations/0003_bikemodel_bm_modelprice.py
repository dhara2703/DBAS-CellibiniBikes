# Generated by Django 2.2.7 on 2019-11-30 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0002_auto_20191130_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='bikemodel',
            name='bm_modelprice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=14),
        ),
    ]
