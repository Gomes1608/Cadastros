# Generated by Django 4.2 on 2023-04-24 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CadastroCliente', '0005_profissao'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profissao',
            options={'verbose_name_plural': 'Profissões'},
        ),
        migrations.AddField(
            model_name='cliente',
            name='profissao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='CadastroCliente.profissao'),
        ),
    ]
