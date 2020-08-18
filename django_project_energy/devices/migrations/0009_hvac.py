# Generated by Django 3.0.9 on 2020-08-10 19:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('devices', '0008_auto_20200809_2134'),
    ]

    operations = [
        migrations.CreateModel(
            name='HVAC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('power', models.CharField(choices=[('Power Saver', 'Power Saver'), ('Normal', 'Normal')], max_length=20)),
                ('temp', models.IntegerField(max_length=5)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
