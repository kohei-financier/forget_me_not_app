# Generated by Django 5.1.5 on 2025-02-17 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("forget_me_not_app", "0006_alter_memo_categories"),
    ]

    operations = [
        migrations.AlterField(
            model_name="memo",
            name="categories",
            field=models.ManyToManyField(blank=True, to="forget_me_not_app.category"),
        ),
    ]
