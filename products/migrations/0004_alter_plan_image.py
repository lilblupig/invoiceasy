# Generated by Django 3.2 on 2022-04-16 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20220414_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='image',
            field=models.ImageField(blank=True, default='noimage.png', null=True, upload_to=''),
        ),
    ]