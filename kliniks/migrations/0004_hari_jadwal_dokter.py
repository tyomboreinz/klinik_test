# Generated by Django 3.2.4 on 2021-08-04 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kliniks', '0003_alter_poli_nama'),
    ]

    operations = [
        migrations.CreateModel(
            name='hari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Jadwal_Dokter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jam_mulai', models.DateTimeField()),
                ('jam_selesai', models.DateTimeField()),
                ('dokter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kliniks.pegawai')),
                ('hari', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kliniks.hari')),
                ('poli', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kliniks.poli')),
            ],
        ),
    ]
