# Generated by Django 4.2.4 on 2024-06-06 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salest_encuesta', models.IntegerField()),
                ('favor_encuesta', models.CharField(max_length=20)),
                ('poraum_encuesta', models.IntegerField()),
                ('ultaum_encuesta', models.CharField(max_length=20)),
                ('razon_encuesta', models.CharField(max_length=80)),
                ('comact_encuesta', models.CharField(max_length=20)),
                ('ventajas_encuesta', models.CharField(max_length=200)),
                ('desventajas_encuesta', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'encuestas',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=200)),
                ('apellido_usuario', models.CharField(max_length=100)),
                ('email_usuario', models.EmailField(max_length=50)),
                ('password_usuario', models.CharField(max_length=80)),
                ('edad_usuario', models.IntegerField()),
                ('telefono_usuario', models.CharField(max_length=9)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'usuarios',
                'ordering': ['-created_at'],
            },
        ),
    ]
