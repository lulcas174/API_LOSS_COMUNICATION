# Generated by Django 4.0 on 2022-01-02 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comunicacao_perda', '0004_alter_farmingproducer_cpf_producer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farming',
            name='farming_event',
            field=models.CharField(choices=[(1, 'Chuva Excessiva'), (2, 'Geada'), (3, 'Granizo'), (4, 'Seca'), (5, 'Vendaval'), (6, 'Raio')], max_length=20),
        ),
    ]
