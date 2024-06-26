# Generated by Django 5.0.4 on 2024-04-09 04:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacionweb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre')),
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='avatarUsuario',
            field=models.ImageField(blank=True, null=True, upload_to='usuarios'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='emailUsuario',
            field=models.CharField(max_length=200, primary_key=True, serialize=False, verbose_name='Email'),
        ),
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('emailAdministrador', models.CharField(max_length=200, primary_key=True, serialize=False, verbose_name='Email')),
                ('nombreAdministrador', models.CharField(max_length=50, verbose_name='Nombre')),
                ('contraseñaAdministrador', models.CharField(max_length=50, verbose_name='Contraseña')),
                ('avatarAdministrador', models.ImageField(blank=True, null=True, upload_to='administradores')),
                ('Categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='administradores', to='aplicacionweb.categoria')),
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='Categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='usuarios', to='aplicacionweb.categoria'),
            preserve_default=False,
        ),
    ]
