# Generated by Django 5.0.6 on 2024-05-09 18:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Warsztaty', '0002_rename_availability_sale_projector_availability'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rezerwacja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('comment', models.TextField(null=True)),
                ('sale_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Warsztaty.sale')),
            ],
            options={
                'unique_together': {('sale_id', 'date')},
            },
        ),
    ]
