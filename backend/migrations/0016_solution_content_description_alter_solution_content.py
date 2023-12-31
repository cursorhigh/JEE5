# Generated by Django 5.0 on 2023-12-11 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0015_rename_contentdescription_question_content_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='content_description',
            field=models.TextField(default='No Context'),
        ),
        migrations.AlterField(
            model_name='solution',
            name='content',
            field=models.ImageField(blank=True, null=True, upload_to='question_images/'),
        ),
    ]
