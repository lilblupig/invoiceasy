# Generated by Django 3.2 on 2022-04-28 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stripecustomer',
            name='trial_ends',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='stripecustomer',
            name='trial_starts',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='stripecustomer',
            name='trial_subs',
            field=models.BooleanField(default=False),
        ),
    ]
