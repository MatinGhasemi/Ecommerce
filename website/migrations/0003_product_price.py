# Generated by Django 4.2.7 on 2023-11-05 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_useraccount_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.PositiveBigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
