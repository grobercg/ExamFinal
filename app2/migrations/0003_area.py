# Generated by Django 4.2.16 on 2024-12-04 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0002_usuario_descripcionusuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreArea', models.CharField(blank=True, max_length=32, null=True)),
                ('descripcionArea', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
    ]
