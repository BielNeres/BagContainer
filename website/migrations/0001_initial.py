# Generated by Django 2.2.7 on 2019-12-10 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=140)),
                ('email', models.EmailField(max_length=254)),
                ('cpf', models.IntegerField()),
                ('dataN', models.DateField()),
                ('mae', models.CharField(max_length=140)),
            ],
        ),
    ]