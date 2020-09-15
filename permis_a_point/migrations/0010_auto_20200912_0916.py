# Generated by Django 2.2.11 on 2020-09-12 09:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('permis_a_point', '0009_conducteur_permis'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='block',
            options={'get_latest_by': 'index', 'ordering': ['index']},
        ),
        migrations.RemoveField(
            model_name='centrestage',
            name='username',
        ),
        migrations.RemoveField(
            model_name='conducteur',
            name='permis',
        ),
        migrations.RemoveField(
            model_name='contravention',
            name='typeC',
        ),
        migrations.AddField(
            model_name='conducteur',
            name='conducteur',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='permis_a_point.Permis'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contravention',
            name='categorie',
            field=models.IntegerField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='agentsecurite',
            name='password',
            field=models.CharField(default='passer', max_length=255),
        ),
        migrations.AlterField(
            model_name='agentsecurite',
            name='username',
            field=models.CharField(default='agent', max_length=15),
        ),
        migrations.AlterField(
            model_name='attestation',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='previous_hash',
            field=models.CharField(default='NIL', max_length=1000),
        ),
        migrations.AlterField(
            model_name='centrestage',
            name='password',
            field=models.CharField(default='passer', max_length=255),
        ),
        migrations.AlterField(
            model_name='conducteur',
            name='password',
            field=models.CharField(default='passer', max_length=255),
        ),
        migrations.AlterField(
            model_name='conducteur',
            name='username',
            field=models.CharField(default='conducteur', max_length=15),
        ),
        migrations.AlterField(
            model_name='contravention',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]