# Generated by Django 3.1.3 on 2020-11-12 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0004_auto_20201112_1742"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Comments",
            new_name="Comment",
        ),
    ]
