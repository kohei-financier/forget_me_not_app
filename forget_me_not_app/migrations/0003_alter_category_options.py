# Generated by Django 5.1.5 on 2025-02-06 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("forget_me_not_app", "0002_category_memo_categories"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "categories"},
        ),
    ]
