# Generated by Django 5.0.4 on 2024-05-01 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0008_pagamento'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagamento',
            name='aprovado',
            field=models.BooleanField(default=False),
        ),
    ]