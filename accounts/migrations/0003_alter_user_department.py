# Generated by Django 4.0.4 on 2022-06-21 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='department',
            field=models.CharField(choices=[('Collections', 'Collections'), ('Billing', 'Billing'), ('Posting', 'Posting')], max_length=200),
        ),
    ]