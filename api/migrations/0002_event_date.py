# Generated by Django 3.0.3 on 2020-02-26 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.CharField(default=0.65, max_length=20),
            preserve_default=False,
        ),
    ]