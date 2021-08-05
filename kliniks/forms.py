from django import forms
from django.forms import ModelForm
from kliniks.models import *

class FormJadwalDokter(ModelForm):
    class Meta:
        model = Jadwal_Dokter
        fields = '__all__'
        # exclude = ['hari']

        widgets = {
            'poli': forms.Select({'class':'form-control'}),
            'dokter': forms.Select({'class':'form-control'}),
            'hari': forms.HiddenInput(),
            'tanggal': forms.DateInput({'type':'date', 'class':'form-control'}),
            'jam_mulai': forms.TimeInput({'type':'time', 'class':'form-control'}),
            'jam_selesai': forms.TimeInput({'type':'time', 'class':'form-control'}),
        }

class FormPoli(ModelForm):
    class Meta:
        model = Poli
        fields = '__all__'

        widgets = {
            'nama': forms.TextInput({'class':'form-control'})
        }

class FormPegawai(ModelForm):
    class Meta:
        model = Pegawai
        fields = '__all__'
        list_kelamin = (
            ('L', 'Laki - Laki'),
            ('P', 'Perempuan'),
        )

        widgets = {
            'nama': forms.TextInput({'class':'form-control'}),
            'nip': forms.TextInput({'class':'form-control'}),
            'jenis_kelamin': forms.Select(choices=list_kelamin,attrs={'class':'form-control'}),
        }
