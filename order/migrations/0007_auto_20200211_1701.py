# Generated by Django 2.2.7 on 2020-02-11 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_auto_20200211_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_no',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]
