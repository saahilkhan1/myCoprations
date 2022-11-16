# Generated by Django 4.1.1 on 2022-09-26 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=200, null=True)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
    ]
