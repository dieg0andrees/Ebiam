# Generated by Django 5.0.4 on 2024-07-28 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('celular', models.CharField(max_length=12)),
                ('correo', models.EmailField(max_length=254)),
                ('mensaje', models.TextField()),
            ],
        ),
    ]
