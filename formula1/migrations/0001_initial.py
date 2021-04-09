# Generated by Django 2.2 on 2021-04-09 06:56

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='F1Track',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('length', models.PositiveIntegerField()),
                ('geometry', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
        ),
    ]