# Generated by Django 2.0.2 on 2018-02-27 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=128)),
                ('last', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128, unique=True)),
            ],
        ),
    ]