# Generated by Django 4.2.16 on 2024-11-02 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_ticket_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket_model',
            name='raised_by',
            field=models.EmailField(max_length=254, verbose_name='Raised By'),
        ),
    ]
