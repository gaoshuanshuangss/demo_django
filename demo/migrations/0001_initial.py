# Generated by Django 3.1.2 on 2020-10-24 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('age', models.IntegerField(max_length=10)),
                ('sex', models.CharField(max_length=32)),
            ],
        ),
    ]
