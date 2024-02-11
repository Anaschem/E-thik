# Generated by Django 3.2.6 on 2024-02-11 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('société', models.CharField(max_length=100)),
                ('nom', models.CharField(max_length=100)),
                ('prénom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('téléphone', models.CharField(max_length=15)),
                ('code_postal', models.CharField(blank=True, max_length=10, null=True)),
                ('ville', models.CharField(blank=True, max_length=100, null=True)),
                ('message', models.TextField()),
                ('types_de_machines', models.CharField(blank=True, max_length=100, null=True)),
                ('distributeur_pains', models.BooleanField(default=False)),
                ('j_accepte_d_etre_contacte', models.BooleanField(default=False)),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
        migrations.DeleteModel(
            name='MenuCategory',
        ),
    ]
