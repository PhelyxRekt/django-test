# Generated by Django 3.2.6 on 2022-04-01 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0002_comentario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='usuarios',
            new_name='usuario',
        ),
    ]
