# Generated by Django 4.0.2 on 2022-02-27 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posting', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
