# Generated by Django 3.1.10 on 2021-05-13 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=12)),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
