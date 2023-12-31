# Generated by Django 5.0 on 2023-12-11 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0016_solution_content_description_alter_solution_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_img', models.ImageField(blank=True, null=True, upload_to='user_images/')),
                ('profile_name', models.CharField(max_length=255)),
                ('profile_id', models.IntegerField(null=True, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='solution',
            name='content',
            field=models.ImageField(blank=True, null=True, upload_to='solution_images/'),
        ),
    ]
