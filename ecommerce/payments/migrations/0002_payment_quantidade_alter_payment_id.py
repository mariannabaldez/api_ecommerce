# Generated by Django 4.2.5 on 2023-09-10 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='quantidade',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='payment',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
