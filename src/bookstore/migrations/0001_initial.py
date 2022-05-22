# Generated by Django 4.0.1 on 2022-05-22 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.CharField(blank=True, max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('authors', models.JSONField(default=list)),
                ('acquired', models.BooleanField(default=False)),
                ('published_year', models.CharField(blank=True, max_length=100)),
                ('thumbnail', models.CharField(blank=True, max_length=300)),
            ],
        ),
    ]
