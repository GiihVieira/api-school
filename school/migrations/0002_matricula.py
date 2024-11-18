# Generated by Django 5.1.3 on 2024-11-13 16:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(choices=[('M', 'Matutino'), ('V', 'Vespertino'), ('N', 'Noturno')], default='M', max_length=1)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.curso')),
                ('estudante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.estudante')),
            ],
        ),
    ]
