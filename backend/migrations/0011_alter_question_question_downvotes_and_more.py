# Generated by Django 5.0 on 2023-12-11 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_alter_question_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_downvotes',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_upvotes',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
