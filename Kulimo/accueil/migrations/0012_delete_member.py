# Generated by Django 4.1.7 on 2023-05-22 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accueil', '0011_alter_message_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Member',
        ),
    ]