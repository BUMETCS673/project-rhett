# Generated by Django 5.0.6 on 2024-06-16 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveys', '0007_response_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='survey',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
