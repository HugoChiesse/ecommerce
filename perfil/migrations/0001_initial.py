# Generated by Django 4.1 on 2022-08-18 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Perfil",
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
                ("idade", models.PositiveBigIntegerField(verbose_name="Idade")),
                (
                    "data_nascimento",
                    models.DateField(verbose_name="Data de Nascimento"),
                ),
                ("cpf", models.CharField(max_length=11, verbose_name="CPF")),
                ("endereco", models.CharField(max_length=50, verbose_name="Endereço")),
                ("numero", models.CharField(max_length=5, verbose_name="Número")),
                (
                    "complemento",
                    models.CharField(max_length=30, verbose_name="Complemento"),
                ),
                ("bairro", models.CharField(max_length=30, verbose_name="Bairro")),
                ("cep", models.CharField(max_length=8, verbose_name="CEP")),
                ("cidade", models.CharField(max_length=30, verbose_name="Cidade")),
                (
                    "estado",
                    models.CharField(
                        choices=[
                            ("AC", "Acre"),
                            ("AL", "Alagoas"),
                            ("AP", "Amapá"),
                            ("AM", "Amazonas"),
                            ("BA", "Bahia"),
                            ("CE", "Ceará"),
                            ("DF", "Distrito Federal"),
                            ("ES", "Espírito Santo"),
                            ("GO", "Goiás"),
                            ("MA", "Maranhão"),
                            ("MT", "Mato Grosso"),
                            ("MS", "Mato Grosso do Sul"),
                            ("MG", "Minas Gerais"),
                            ("PA", "Pará"),
                            ("PB", "Paraíba"),
                            ("PR", "Paraná"),
                            ("PE", "Pernambuco"),
                            ("PI", "Piauí"),
                            ("RJ", "Rio de Janeiro"),
                            ("RN", "Rio Grande do Norte"),
                            ("RS", "Rio Grande do Sul"),
                            ("RO", "Rondônia"),
                            ("RR", "Roraima"),
                            ("SC", "Santa Catarina"),
                            ("SP", "São Paulo"),
                            ("SE", "Sergipe"),
                            ("TO", "Tocantins"),
                        ],
                        default="SP",
                        max_length=2,
                    ),
                ),
                (
                    "usuario",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Usuário",
                    ),
                ),
            ],
            options={"verbose_name": "Perfil", "verbose_name_plural": "Perfis",},
        ),
    ]
