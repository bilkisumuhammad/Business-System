# Generated by Django 5.0.1 on 2024-02-23 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('purchase_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('additional_costs', models.DecimalField(decimal_places=2, default=10, max_digits=10)),
                ('total_amount', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('purchase_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
