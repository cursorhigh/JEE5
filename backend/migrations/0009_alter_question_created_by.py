# Generated by Django 5.0 on 2023-12-11 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_question_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='created_by',
            field=models.CharField(default='Unknown', max_length=255, null=True),
        ),
    ]
