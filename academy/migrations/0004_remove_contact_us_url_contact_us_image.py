# Generated by Django 4.2.4 on 2023-11-07 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0003_remove_blog_description_remove_courses_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact_us',
            name='url',
        ),
        migrations.AddField(
            model_name='contact_us',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to=''),
        ),
    ]
