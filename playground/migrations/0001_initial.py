# Generated by Django 4.1.3 on 2022-12-04 21:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('edad', models.IntegerField(max_length=2)),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('X', 'Otro')], max_length=1)),
                ('parentesco', models.CharField(choices=[('Primo', 'Primo'), ('Padre', 'Padre'), ('Madre', 'Madre'), ('Abuelo', 'Abuelo'), ('Hermano', 'Hermano')], max_length=20)),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]