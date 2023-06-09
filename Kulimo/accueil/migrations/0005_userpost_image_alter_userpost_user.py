# Generated by Django 4.1.7 on 2023-05-01 19:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accueil', '0004_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpost',
            name='image',
            field=models.ImageField(default='/static/img/default.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='userpost',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='userposts', to=settings.AUTH_USER_MODEL),
        ),
    ]
