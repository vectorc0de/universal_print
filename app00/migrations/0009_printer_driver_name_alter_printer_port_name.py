# Generated by Django 4.2 on 2023-04-17 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app00", "0008_alter_printer_port_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="printer",
            name="driver_name",
            field=models.CharField(default="", max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="printer",
            name="port_name",
            field=models.CharField(max_length=64),
        ),
    ]
