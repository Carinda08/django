# Generated by Django 3.2.4 on 2021-06-19 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=30, unique=True)),
                ('upwd', models.CharField(max_length=30)),
            ],
        ),
    ]
