# Generated by Django 2.2 on 2020-08-13 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgentSecurite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='agent', max_length=15)),
                ('prenom', models.CharField(max_length=60)),
                ('nom', models.CharField(max_length=40)),
                ('matricule', models.IntegerField()),
                ('password', models.CharField(default='passer', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('donnees', models.TextField()),
                ('previous_hash', models.CharField(default='NIL', max_length=1000)),
                ('hash_block', models.CharField(max_length=1000)),
            ],
            options={
                'ordering': ['index'],
                'get_latest_by': 'index',
            },
        ),
        migrations.CreateModel(
            name='CentreStage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=40)),
                ('adresse', models.CharField(max_length=40)),
                ('password', models.CharField(default='passer', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Conducteur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(default='conducteur', max_length=15)),
                ('password', models.CharField(default='passer', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Permis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=60)),
                ('nom', models.CharField(max_length=40)),
                ('date_naissance', models.DateField()),
                ('lieu_naissance', models.CharField(max_length=40)),
                ('date_delivrance', models.DateField()),
                ('date_expiration', models.DateField()),
                ('numero', models.IntegerField()),
                ('groupe_sanguin', models.CharField(max_length=3)),
                ('categorie_vehicule', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('conducteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='permis_a_point.Conducteur')),
            ],
        ),
        migrations.CreateModel(
            name='Contravention',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('categorie', models.IntegerField()),
                ('contenu', models.TextField()),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='permis_a_point.AgentSecurite')),
                ('destinataire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='permis_a_point.Conducteur')),
            ],
        ),
        migrations.AddField(
            model_name='conducteur',
            name='conducteur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='permis_a_point.Permis'),
        ),
        migrations.CreateModel(
            name='Attestation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('contenu', models.TextField()),
                ('centre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='permis_a_point.CentreStage')),
                ('stagiaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='permis_a_point.Conducteur')),
            ],
        ),
    ]
