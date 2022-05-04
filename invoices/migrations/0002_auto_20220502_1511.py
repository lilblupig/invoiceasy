# Generated by Django 3.2 on 2022-05-02 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('invoices', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoicecustomer',
            name='invoice_customer_id',
        ),
        migrations.AddField(
            model_name='invoicecustomer',
            name='customer_code',
            field=models.CharField(default='default', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='invoicecustomer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]