# Generated by Django 5.0.6 on 2024-06-15 11:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0004_response_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveys.question'),
        ),
    ]
