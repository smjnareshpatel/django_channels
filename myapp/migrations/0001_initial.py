# Generated by Django 3.2.6 on 2021-08-14 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserJsonData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=500, null=True)),
                ('indicator', models.CharField(blank=True, max_length=500, null=True)),
                ('value', models.CharField(blank=True, max_length=500, null=True)),
                ('year', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
