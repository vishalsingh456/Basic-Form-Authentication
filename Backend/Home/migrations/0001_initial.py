# Generated by Django 4.1.2 on 2023-03-12 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=225, null=True)),
                ('dob', models.DateField()),
                ('email', models.EmailField(blank=True, max_length=225, null=True)),
            ],
        ),
    ]
