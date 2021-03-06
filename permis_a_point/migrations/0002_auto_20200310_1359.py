# Generated by Django 2.2.11 on 2020-03-10 12:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('permis_a_point', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgentSecurite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=60)),
                ('nom', models.CharField(max_length=40)),
                ('matricule', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CentreStage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=40)),
                ('adresse', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Conducteur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('conducteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='permis_a_point.Permis')),
            ],
        ),
        migrations.AddField(
            model_name='contravention',
            name='contenu',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contravention',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contravention',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='permis_a_point.AgentSecurite'),
        ),
        migrations.AlterField(
            model_name='contravention',
            name='destinataire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='permis_a_point.Conducteur'),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('conducteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='permis_a_point.Conducteur')),
            ],
        ),
        migrations.CreateModel(
            name='Attestation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('contenu', models.TextField()),
                ('centre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='permis_a_point.CentreStage')),
                ('stagiaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='permis_a_point.Conducteur')),
            ],
        ),
    ]
