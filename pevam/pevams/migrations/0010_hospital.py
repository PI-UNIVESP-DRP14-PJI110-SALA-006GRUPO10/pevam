# Generated by Django 5.1.1 on 2024-10-31 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pevams', '0009_alter_local_cidade_alter_local_complemento_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('logradouro', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=5)),
                ('complemento', models.CharField(blank=True, max_length=15, null=True)),
                ('bairro', models.CharField(max_length=25)),
                ('cidade', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=8)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('telefone', models.CharField(max_length=10)),
            ],
        ),
    ]
