from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Hari(models.Model):
    nama = models.CharField(max_length=15)
    nama_indo = models.CharField(max_length=6)

    def __str__(self):
        return self.nama_indo

class Poli(models.Model):
    nama = models.CharField(max_length=40)

    def __str__(self):
        return self.nama

class Pegawai(models.Model):
    nama = models.CharField(max_length=40)
    nip = models.CharField(max_length=15)
    jenis_kelamin = models.CharField(max_length=1)

    def __str__(self):
        return self.nama

class Jadwal_Dokter(models.Model):
    poli = models.ForeignKey(Poli, on_delete=models.CASCADE)
    dokter = models.ForeignKey(Pegawai, on_delete=models.CASCADE)
    hari = models.ForeignKey(Hari, on_delete=models.CASCADE, null=True)
    tanggal = models.DateField(null=True)
    jam_mulai = models.TimeField()
    jam_selesai = models.TimeField()
    
