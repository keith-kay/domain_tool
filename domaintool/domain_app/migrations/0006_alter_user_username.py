# Generated by Django 4.2.7 on 2023-12-19 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain_app', '0005_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
