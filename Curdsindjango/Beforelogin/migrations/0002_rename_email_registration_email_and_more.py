# Generated by Django 4.1.1 on 2022-09-26 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Beforelogin', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='registration',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='registration',
            old_name='Password',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='registration',
            old_name='Phone',
            new_name='phone',
        ),
    ]
