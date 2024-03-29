# Generated by Django 3.2.6 on 2024-02-22 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0008_alter_products_label'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='ecommerce.basemodel')),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.products')),
            ],
            bases=('ecommerce.basemodel',),
        ),
    ]
