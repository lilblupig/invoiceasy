# Generated by Django 3.2 on 2022-04-14 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_plans_plan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='image_url',
        ),
        migrations.AddField(
            model_name='plan',
            name='duration',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='plan',
            name='image_alt',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]