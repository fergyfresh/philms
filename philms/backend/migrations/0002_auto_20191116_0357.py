# Generated by Django 2.2.7 on 2019-11-16 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='code',
            field=models.CharField(db_index=True, max_length=4),
        ),
    ]
