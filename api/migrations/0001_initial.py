# Generated by Django 5.1.6 on 2025-02-06 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('last_connection', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('website', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('followers', models.IntegerField()),
                ('following', models.IntegerField()),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
