# Generated by Django 3.2.25 on 2025-01-14 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_portfolio_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='mini_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
