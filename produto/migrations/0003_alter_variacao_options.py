# Generated by Django 4.1 on 2022-08-10 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("produto", "0002_alter_produto_descricao_longa_variacao"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="variacao",
            options={"verbose_name": "Variação", "verbose_name_plural": "Variações"},
        ),
    ]
