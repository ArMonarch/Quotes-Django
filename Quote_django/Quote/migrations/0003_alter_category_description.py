# Generated by Django 4.2.3 on 2023-07-28 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quote', '0002_alter_category_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='Description',
            field=models.TextField(blank=True, null=True),
        ),
    ]