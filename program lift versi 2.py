import tkinter as bk  # Blom selesai updatenya, udah cape mau tidur besok lagi aja
# kalau pake gird() untuk label, jangan menggunakan StringVar() kalau mau textnya berubah
# tapi pakai configure(text=""), karna kalo ini bakal nunjukkin textnya, tapi kalo StringVar() ga bakal

# belom selesai tapi ada beberapa masalah yang telah terselesaikan, masalah senaljutnya: ngambil input nama lantai
# udah selesai semuanya sekarang

# fitur tidak akan diupdate lagi

layar = bk.Tk()
layar.geometry("300x400")
layar_2 = bk.Tk()
layar_2.geometry("500x200")
tulisan_ajaib = bk.StringVar()
format_posisi_ajaib = bk.StringVar()
input_lantai = bk.StringVar()
format_posisi_ajaib.set("Anda berada di ")
lantai_berapa = "Lantai Dasar"
tulisan_ajaib.set("Lantai Dasar")
format_lantai, pilihan = "Sekarang kita berada di lantai ", "TUTUP"
lantai, penanda_batasan = 4, 1
susunan_lantai = ["B3", "B2", "B1", "LG", "G", "UG", "1", "2", "3", "4", "5", "6", "7", "Rooftop"]  # total 14 lantai
# ground di lantai ke 4 pada awalnya


class PembuatanLantaiBaru:
    nama_lantai_baru = bk.Entry(layar_2, bd=3, textvariable=input_lantai)
    tombol_konfirmasi_1 = bk.Button(layar_2, text="Iya", command=lambda: plb.lantai_baru("IYA"))
    tombol_konfirmasi_2 = bk.Button(layar_2, text="Tidak", command=lambda: plb.lantai_baru("TIDAK"))
    tombol_konfirmasi_3 = bk.Button(layar_2, text="Konfirmasi nama lantai",
                                    command=lambda: plb.menambah_lantai_atau_menutup(pilihan))
    tulisan_konfirmasi = bk.Label(layar_2, text="Apakah anda ingin membuat lantai baru?", bg="#c6f653")

    def __init__(self):
        pass

    @staticmethod
    def mulai():
        plb.tulisan_konfirmasi.grid(row=0, column=1, columnspan=3)
        plb.tombol_konfirmasi_1.grid(row=1, column=1)
        plb.tombol_konfirmasi_2.grid(row=1, column=3)

    @staticmethod
    def tambah_lantai():
        global penanda_batasan
        if penanda_batasan >= 6:
            susunan_lantai.append(plb.nama_lantai_baru.get())
        elif penanda_batasan <= -6:
            susunan_lantai.insert(0, plb.nama_lantai_baru.get())
        plb.nama_lantai_baru.delete(0, last=bk.END)
        layar_2.after(2100, plb.nama_lantai_baru.grid_remove())
        penanda_batasan = 0
        plb.tulisan_konfirmasi.grid_remove()
        plb.tombol_konfirmasi_3.grid_remove()
        fu.tombol_naik.configure(state=bk.NORMAL, relief=bk.RAISED)
        fu.tombol_turun.configure(state=bk.NORMAL, relief=bk.RAISED)

    @staticmethod
    def menambah_lantai_atau_menutup(keputusan):
        if keputusan == "TAMBAH":
            plb.tambah_lantai()
        elif keputusan == "TUTUP":
            plb.tutup()

    @staticmethod
    def lantai_baru(konfirmasi):
        global susunan_lantai, pilihan
        posisi = 3
        plb.tombol_konfirmasi_1.grid_remove()
        plb.tombol_konfirmasi_2.grid_remove()
        if konfirmasi == "TIDAK":
            plb.tombol_konfirmasi_3.configure(text="Tutup")
            pilihan = "TUTUP"
            posisi = 2
            plb.tulisan_konfirmasi.configure(text="Baiklah")
        elif konfirmasi == "IYA":
            plb.tombol_konfirmasi_3.configure(text="Konfirmasi nama lantai")
            pilihan = "TAMBAH"
            plb.tulisan_konfirmasi.configure(text="Masukkan nama lantai yang ingin anda tambahkan:")
            plb.nama_lantai_baru.grid(row=1, column=0, columnspan=3)
            plb.nama_lantai_baru.icursor(0)
        plb.tombol_konfirmasi_3.grid(row=1, column=posisi)

        # utama()

    @staticmethod
    def tutup():
        global penanda_batasan
        penanda_batasan = 0
        plb.tulisan_konfirmasi.configure(text="Apakah anda ingin membuat lantai baru?")
        plb.tulisan_konfirmasi.grid_remove()
        plb.tombol_konfirmasi_3.grid_remove()
        fu.tombol_naik.configure(state=bk.NORMAL, relief=bk.RAISED)
        fu.tombol_turun.configure(state=bk.NORMAL, relief=bk.RAISED)

    # batas class


plb = PembuatanLantaiBaru()


class FungsiUtama:
    tombol_naik = bk.Button(layar_2, text="Naik 1 lantai",
                            command=lambda: naik_atau_turun("NAIK"), state=bk.NORMAL, relief=bk.RAISED)
    tombol_turun = bk.Button(layar_2, text="Turun 1 lantai",
                             command=lambda: naik_atau_turun("TURUN"), state=bk.NORMAL, relief=bk.RAISED)
    tulisan = bk.Label(layar, textvariable=tulisan_ajaib, bg="#f7ff9c", relief=bk.SUNKEN)
    format_posisi = bk.Label(layar, textvariable=format_posisi_ajaib, bg="#cdff6e", relief=bk.RAISED)


fu = FungsiUtama()


def lokasi_lantai(tempat):
    global lantai_berapa, lantai, penanda_batasan, susunan_lantai
    lokasi = "G"
    ukuran_list = len(susunan_lantai) - 1
    if tempat < 0:
        format_posisi_ajaib.set("Ini adalah lantai terendah!")
        penanda_batasan = penanda_batasan - 1
        tempat, lantai = 0, 0
        lokasi = susunan_lantai[0]
    elif tempat > ukuran_list:
        format_posisi_ajaib.set("Ini adalah lantai tertinggi!")
        penanda_batasan = penanda_batasan + 1
        tempat, lantai = ukuran_list, ukuran_list
        lokasi = susunan_lantai[ukuran_list]
    elif 0 <= tempat <= ukuran_list:
        format_posisi_ajaib.set("Anda berada di")
        penanda_batasan = 0
        lokasi = susunan_lantai[tempat]
    return lokasi


def naik_atau_turun(tujuan):
    global lantai_berapa, lantai

    if penanda_batasan >= 6 or penanda_batasan <= -6:  # dengan batasan 6, memerlukan 7 kali pencetan tombol.
        # ya ga terlalu masalah sih
        fu.tombol_naik.configure(state=bk.DISABLED, relief=bk.FLAT)
        fu.tombol_turun.configure(state=bk.DISABLED, relief=bk.FLAT)
        plb.mulai()

    if tujuan == "NAIK":
        lantai = lantai + 1
    elif tujuan == "TURUN":
        lantai = lantai - 1
    lantai_berapa = "Lantai " + lokasi_lantai(lantai)
    tulisan_ajaib.set(lantai_berapa)

    # utama()


def utama():
    global tulisan_ajaib, penanda_batasan

    fu.tombol_naik.grid(row=2, column=2, pady=2)
    fu.tombol_turun.grid(row=3, column=2, pady=2)
    fu.format_posisi.pack(pady=1)
    fu.tulisan.pack(pady=1)

    layar.mainloop()

    layar_2.mainloop()


utama()

# batas
