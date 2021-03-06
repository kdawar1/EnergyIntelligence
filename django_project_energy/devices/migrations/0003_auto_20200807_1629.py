# Generated by Django 3.0.9 on 2020-08-07 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0002_device_is_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='is_entertainment',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=15),
        ),
        migrations.AlterField(
            model_name='device',
            name='is_on',
            field=models.CharField(choices=[('On', 'On'), ('Off', 'Off')], default='Off', max_length=15),
        ),
    ]
