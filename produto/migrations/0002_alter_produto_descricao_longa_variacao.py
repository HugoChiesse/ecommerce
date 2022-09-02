# Generated by Django 4.1 on 2022-08-10 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("produto", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produto",
            name="descricao_longa",
            field=models.TextField(verbose_name="Descrição Longa"),
        ),
        migrations.CreateModel(
            name="Variacao",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nome",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Nome"
                    ),
                ),
                ("preco", models.FloatField(verbose_name="Preço")),
                (
                    "preco_promocional",
                    models.FloatField(default=0, verbose_name="Preço Promocional"),
                ),
                (
                    "estoque",
                    models.PositiveIntegerField(default=1, verbose_name="Estoque"),
                ),
                (
                    "produto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="produto.produto",
                        verbose_name="Produto",
                    ),
                ),
            ],
        ),
    ]
