# Generated by Django 5.0.1 on 2024-02-18 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_publicacao_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacao',
            name='imagem',
            field=models.CharField(max_length=20),
        ),
    ]
