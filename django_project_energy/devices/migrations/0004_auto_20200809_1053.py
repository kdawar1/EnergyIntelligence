# Generated by Django 3.0.9 on 2020-08-09 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0003_auto_20200807_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.CharField(choices=[('Bedroom', 'Bedroom'), ('Bathroom', 'Bathroom'), ('Kitchen', 'Kitchen'), ('Living Room', 'Living Room'), ('Dining Room', 'Dining Room'), ('Closet', 'Closet'), ('Other', 'Other')], max_length=15),
        ),
    ]
