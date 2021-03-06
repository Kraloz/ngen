# Generated by Django 2.1.2 on 2018-11-10 23:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cultivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_estimada', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Germinacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_estimada', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('dias_germinacion', models.IntegerField()),
                ('maceta_litros', models.IntegerField()),
                ('riego', models.CharField(max_length=150)),
                ('etapa_recoleccion', models.CharField(max_length=150)),
                ('extra', models.TextField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='germinacion',
            name='planta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Planta'),
        ),
        migrations.AddField(
            model_name='cultivo',
            name='planta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Planta'),
        ),
    ]
