# Generated by Django 4.0.5 on 2022-06-10 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [migrations.RenameModel("Highscore", "Score")]
