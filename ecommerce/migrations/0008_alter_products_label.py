# Generated by Django 3.2.6 on 2024-02-22 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0007_auto_20240222_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='label',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
