# Generated by Django 5.1.3 on 2024-11-24 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_category1'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(default=1, upload_to=True),
            preserve_default=False,
        ),
    ]
