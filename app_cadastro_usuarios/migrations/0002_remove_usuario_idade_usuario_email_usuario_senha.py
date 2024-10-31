# Generated by Django 5.1.2 on 2024-10-31 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cadastro_usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='idade',
        ),
        migrations.AddField(
            model_name='usuario',
            name='email',
            field=models.EmailField(default='enteryour@email.com', max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='senha',
            field=models.TextField(default='default_password'),
        ),
    ]
