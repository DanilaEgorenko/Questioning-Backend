# Generated by Django 4.1.3 on 2023-01-14 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0011_emailreceivers_historicalemailreceivers"),
    ]

    operations = [
        migrations.AlterField(
            model_name="emailreceivers",
            name="id",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to="main.user",
            ),
        ),
        migrations.AlterField(
            model_name="premiumuser",
            name="id",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                primary_key=True,
                serialize=False,
                to="main.user",
            ),
        ),
    ]
