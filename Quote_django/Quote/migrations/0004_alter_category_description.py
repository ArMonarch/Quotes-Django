# Generated by Django 4.2.3 on 2023-07-28 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quote', '0003_alter_category_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='Description',
            field=models.CharField(default='Description', max_length=255, null=True),
        ),
    ]