# Generated by Django 5.0 on 2023-12-31 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_ai', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='Code_ai',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Tên danh mục'),
        ),
    ]
