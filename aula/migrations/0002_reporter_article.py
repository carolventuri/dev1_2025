# Generated by Django 5.1.7 on 2025-03-25 00:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aula', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reporter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Escreva aqui o nome do reporter.', max_length=100, verbose_name='Nome:')),
                ('email', models.EmailField(help_text='Escreva aqui o email.', max_length=100, verbose_name='Email:')),
                ('cpf', models.CharField(help_text='Escreva aqui o CPF.', max_length=11, verbose_name='CPF:')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Escreva aqui o título do Artigo.', max_length=100, verbose_name='Nome:')),
                ('pub_date', models.DateField(help_text='Escreva aqui a data de publicação', verbose_name='Data publicação:')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aula.reporter')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
