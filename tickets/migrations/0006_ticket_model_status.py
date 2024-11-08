# Generated by Django 4.2.16 on 2024-11-03 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0005_alter_ticket_model_raised_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket_model',
            name='status',
            field=models.CharField(blank=True, choices=[('Reported', 'Reported'), ('InProgress', 'In Progress'), ('Solved', 'Solved')], max_length=30, null=True, verbose_name='Status'),
        ),
    ]
