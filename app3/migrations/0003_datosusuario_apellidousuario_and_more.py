# Generated by Django 4.2.16 on 2024-12-21 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app3', '0002_publicacion_imagenpub_alter_comentario_autocom_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosusuario',
            name='apellidoUsuario',
            field=models.CharField(blank=True, max_length=48, null=True),
        ),
        migrations.AddField(
            model_name='datosusuario',
            name='contraUsuario',
            field=models.CharField(blank=True, max_length=48, null=True),
        ),
        migrations.AddField(
            model_name='datosusuario',
            name='nombreUsuario',
            field=models.CharField(blank=True, max_length=48, null=True),
        ),
        migrations.AddField(
            model_name='datosusuario',
            name='usernameUsuario',
            field=models.CharField(blank=True, max_length=48, null=True),
        ),
    ]
