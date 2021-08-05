from django.http.response import FileResponse, HttpResponse
from django.shortcuts import redirect, render

from kliniks.models import *
from kliniks.forms import *
from klinik.utils import render_to_pdf

import datetime, reportlab, io
from datetime import date
from reportlab.pdfgen import canvas

# locale.setlocale(locale.LC_TIME, 'en_ID.UTF-8')

def coba_cetak(request):
    jadwal = Poli.objects.raw("""
        select jd.id, poli.nama as poli, pg.nama,
        case when hari_id=1 then (select jam_mulai ||' - '|| jam_selesai from kliniks_jadwal_dokter where hari_id=1 and poli_id=jd.poli_id) end as senin,
        case when hari_id=2 then (select jam_mulai ||' - '|| jam_selesai from kliniks_jadwal_dokter where hari_id=2 and poli_id=jd.poli_id) end as selasa,
        case when hari_id=3 then (select jam_mulai ||' - '|| jam_selesai from kliniks_jadwal_dokter where hari_id=3 and poli_id=jd.poli_id) end as rabu,
        case when hari_id=4 then (select jam_mulai ||' - '|| jam_selesai from kliniks_jadwal_dokter where hari_id=4 and poli_id=jd.poli_id) end as kamis,
        case when hari_id=5 then (select jam_mulai ||' - '|| jam_selesai from kliniks_jadwal_dokter where hari_id=5 and poli_id=jd.poli_id) end as jumat,
        case when hari_id=6 then (select jam_mulai ||' - '|| jam_selesai from kliniks_jadwal_dokter where hari_id=6 and poli_id=jd.poli_id) end as sabtu,
        case when hari_id=7 then (select jam_mulai ||' - '|| jam_selesai from kliniks_jadwal_dokter where hari_id=7 and poli_id=jd.poli_id) end as minggu
        from kliniks_jadwal_dokter jd
        left join kliniks_poli poli on poli.id = jd.poli_id
        LEFT JOIN kliniks_pegawai pg on pg.id = jd.dokter_id""")
    data = {
        'jadwal': jadwal,
    }
    pdf = render_to_pdf('jadwal_cetak.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

def cetak(request):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 100, "hai hai")
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hai.pdf')

def jadwal_cetak(request):
    jadwal = Poli.objects.raw("""select jd.id, poli.nama as poli, pg.nama,

case when hari_id=1 then (select jam_mulai ||' - '|| jam_selesai from kliniks_jadwal_dokter where hari_id=1 and poli_id=jd.poli_id) end as senin,
case when hari_id=2 then (select jam_mulai ||' - '|| jam_selesai from kliniks_jadwal_dokter where hari_id=2 and poli_id=jd.poli_id) end as selasa,
case when hari_id=3 then (select jam_mulai ||' - '|| jam_selesai from kliniks_jadwal_dokter where hari_id=3 and poli_id=jd.poli_id) end as rabu,
case when hari_id=4 then (select jam_mulai ||' - '|| jam_selesai from kliniks_jadwal_dokter where hari_id=4 and poli_id=jd.poli_id) end as kamis,
case when hari_id=5 then (select jam_mulai ||' - '|| jam_selesai from kliniks_jadwal_dokter where hari_id=5 and poli_id=jd.poli_id) end as jumat,
case when hari_id=6 then (select jam_mulai ||' - '|| jam_selesai from kliniks_jadwal_dokter where hari_id=6 and poli_id=jd.poli_id) end as sabtu,
case when hari_id=7 then (select jam_mulai ||' - '|| jam_selesai from kliniks_jadwal_dokter where hari_id=7 and poli_id=jd.poli_id) end as minggu

from kliniks_jadwal_dokter jd
left join kliniks_poli poli on poli.id = jd.poli_id
LEFT JOIN kliniks_pegawai pg on pg.id = jd.dokter_id""")
    data = {
        'jadwal': jadwal,
    }
    return render(request, 'jadwal_cetak.html', data)

def jadwal_hapus(request, id_jadwal):
    jadwal = Jadwal_Dokter.objects.get(id=id_jadwal)
    jadwal.delete()
    return redirect('/jadwal')

def jadwal_edit(request, id_jadwal):
    jadwal = Jadwal_Dokter.objects.get(id=id_jadwal)
    if request.POST:
        post_value = request.POST.copy()
        year, month, day = str(post_value['tanggal']).split('-')
        nama_hari = datetime.date(int(year), int(month), int(day))
        print(nama_hari.strftime('%A'))
        hari = Hari.objects.get(nama=nama_hari.strftime('%A'))
        post_value['hari'] = hari.id
        form = FormJadwalDokter(post_value, instance=jadwal)
        if form.is_valid():
            form.save()
            return redirect('/jadwal')
    else:
        form = FormJadwalDokter(instance=jadwal)
        data = {
            'form' : form,
            'title' : 'Edit Jadwal',
        }
    return render(request, 'edit.html', data)

def jadwal_tambah(request):
    if request.POST:
        post_value = request.POST.copy()
        year, month, day = str(post_value['tanggal']).split('-')
        nama_hari = datetime.date(int(year), int(month), int(day))
        hari = Hari.objects.get(nama=nama_hari.strftime('%A'))
        post_value['hari'] = hari.id
        form = FormJadwalDokter(post_value)
        if form.is_valid():
            form.save()
            return redirect('/jadwal')
    else:
        form = FormJadwalDokter()
        data = {
            'form' : form,
            'title' : 'Tambah Jadwal',
        }
    return render(request, 'tambah.html', data)

def jadwal(request):
    jadwal = Jadwal_Dokter.objects.all()
    data = {
        'jadwal' : jadwal,
        'active_jadwal' : 'active'
    }
    return render(request, 'jadwal.html', data)

def poli_hapus(request, id_poli):
    poli = Pegawai.objects.get(id=id_poli)
    poli.delete()
    return redirect('/poli')

def poli_edit(request, id_poli):
    poli = Poli.objects.get(id=id_poli)
    if request.POST:
        form = FormPoli(request.POST, instance=poli)
        if form.is_valid():
            form.save()
            return redirect('/poli')
    else:
        form = FormPoli(instance=poli)
        data = {
            'form' : form,
            'title' : 'Edit Poli',
        }
    return render(request, 'edit.html', data)

def poli_tambah(request):
    if request.POST:
        form = FormPoli(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/poli')
    else:
        form = FormPoli()
        data = {
            'form' : form,
            'title' : 'Tambah Poli',
        }
    return render(request, 'tambah.html', data)

def poli(request):
    poli = Poli.objects.all()
    data = {
        'poli' : poli,
        'active_poli' : 'active'
    }
    return render(request, 'poli.html', data)

def pegawai_hapus(request, id_pegawai):
    pegawai = Pegawai.objects.get(id=id_pegawai)
    pegawai.delete()
    return redirect('/')

def pegawai_edit(request, id_pegawai):
    pegawai = Pegawai.objects.get(id=id_pegawai)
    if request.POST:
        form = FormPegawai(request.POST, instance=pegawai)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = FormPegawai(instance=pegawai)
        data = {
            'form' : form,
            'title' : 'Edit Pegawai',
        }
    return render(request, 'edit.html', data)

def pegawai_tambah(request):
    if request.POST:
        form = FormPegawai(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = FormPegawai()
        data = {
            'form' : form,
            'title' : 'Tambah Pegawai',
        }
    return render(request, 'tambah.html', data)

def pegawai(request):
    pegawai = Pegawai.objects.all()
    data = {
        'pegawai' : pegawai,
        'active_pegawai' : 'active'
    }
    return render(request, 'pegawai.html', data)