# Generated by Django 5.0.7 on 2024-07-20 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='user_email',
            field=models.EmailField(default='default@example.com', max_length=254),
        ),
    ]
