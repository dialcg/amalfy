# Generated by Django 2.1.3 on 2018-11-26 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('content', models.TextField()),
                ('order', models.PositiveIntegerField(unique=True)),
            ],
        ),
    ]
