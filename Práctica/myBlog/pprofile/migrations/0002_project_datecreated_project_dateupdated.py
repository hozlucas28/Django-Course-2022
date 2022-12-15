# Generated by Django 4.1.4 on 2022-12-15 02:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("pprofile", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="dateCreated",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="project",
            name="dateUpdated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
