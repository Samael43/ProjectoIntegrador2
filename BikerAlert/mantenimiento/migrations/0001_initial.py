# Generated by Django 5.1.2 on 2024-10-13 23:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('motocicleta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoMantenimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mantenimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_realizacion', models.DateField()),
                ('proxima_fecha_realizacion', models.DateField(blank=True, null=True)),
                ('observaciones', models.TextField(blank=True)),
                ('motocicleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='motocicleta.motocicleta')),
                ('tipo_mantenimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mantenimiento.tipomantenimiento')),
            ],
        ),
    ]
