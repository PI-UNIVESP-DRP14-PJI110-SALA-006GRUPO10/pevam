# Generated by Django 5.1.1 on 2024-10-08 00:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pevams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContatoEmergencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_contato', models.CharField(max_length=100)),
                ('telefone_contato', models.CharField(max_length=15)),
                ('cadastro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pevams.cadastro')),
            ],
        ),
    ]
