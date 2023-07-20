import tkinter as bk  # kalo mau buat app make terminal dan namanya ada space ditulis pake ' '
import os
from PIL import Image, ImageTk
# import manipulator_File as mf

# membuat gambar dari gedungnya, atau menggunakan paint trus diapain bisa lah
# beberapa update udah dilakukan, untuk saat ini GUI jadul juga gapapa
# perlu mengoptimalkan fitur tambah lantai saat mentok, karena tombolnya tidak muncul apabila sudah di tambah
# update akan segera di tambahkan, untuk saat ini sudah ada tombol fitur komplex dan simple, serta fitur lainnya
# yang ada di fitur komplex

# tambahin colour palete jadi lebih modern, lebih sleek
# update nanti

layar = bk.Tk()  # warna bg="#2e2d2c
layar.geometry("680x340")
layar.title("Lift Mania")
layar.iconbitmap("icon lift mania.ico")
bingkai_utama = bk.LabelFrame(layar)  # warna bg="#383635
bingkai_1 = bk.LabelFrame(bingkai_utama, text="Pengendali", bg="#ffe9cb", padx=10, pady=10, borderwidth=5, border=5)
bingkai_2 = bk.LabelFrame(bingkai_utama, text="Tampilan Utama", bg="#ffedb0", padx=10, pady=10, borderwidth=5, border=5)
bingkai_3 = bk.LabelFrame(bingkai_utama, text="Spesifikasi Bangungan",
                          bg="#d5dfff", pady=10, padx=10, borderwidth=5, border=5)
bingkai_4 = bk.LabelFrame(bingkai_utama, text="Mengubah Tipe Apartemen",
                          bg="#ffa97f", padx=10, pady=10, borderwidth=5, border=5)
bingkai_5 = bk.LabelFrame(bingkai_utama, padx=10, pady=10, borderwidth=5, border=5)
bingkai_6 = bk.LabelFrame(bingkai_utama, text="Background", pady=10, padx=10, borderwidth=5, border=5, bg="#484645")
gambar_lantai_gedung = ImageTk.PhotoImage(Image.open("D:/Persiapan-Kuliah/program python/Lantai Gedung/Lantai G.png"))
tulisan_ajaib = bk.StringVar()
format_posisi_ajaib = bk.StringVar()
tulisan_gedung_ajaib = bk.StringVar()
penentu_background = bk.StringVar()
input_lantai = bk.StringVar()
format_spinbox_ajaib = bk.StringVar()
format_posisi_ajaib.set("Anda berada di ")
lantai_berapa = "Lantai G"
tulisan_ajaib.set("Lantai G")
format_lantai, pilihan = "Sekarang kita berada di lantai ", "TUTUP"
lantai, penanda_batasan, penanda_tampil, penanda_hapus, penanda_fitur = 4, 1, 0, 0, 0
susunan_lantai = ["B3", "B2", "B1", "LG", "G", "UG", "1", "2", "3", "4", "5", "6", "7", "Rooftop"]  # total 14 lantai
alamat = "D:/Persiapan-Kuliah/program python/Jenis Gedung"
lantai_pada_gedung = os.listdir(alamat)
urutan_lantai = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]  # mathcing dengan susunan lantainya
# ground pada Apartement 1 ada di 4
# ground pada Apartement 2 ada di 2
# ground pada Apartement 3 ada di 1
# ground pada Apartement 4 ada di 0
# ground pada Apartement 5 ada di 0
# ground pada Apartement 6 ada di 8
# ground pada Apartement 7 ada di 2


def utama(penanda):
    global tulisan_ajaib, penanda_batasan, penanda_fitur

    fu.tombol_naik.configure(state=bk.NORMAL, relief=bk.RAISED)
    fu.tombol_turun.configure(state=bk.NORMAL, relief=bk.RAISED)
    fu.tombol_semua_lantai.configure(state=bk.NORMAL, relief=bk.GROOVE)
    fu.tombol_menghapus_lantai.configure(state=bk.NORMAL, relief=bk.RAISED)
    fu.spinbox_lantai.configure(state=bk.NORMAL, relief=bk.RAISED)
    fu.tombol_menambah_lantai.configure(state=bk.NORMAL, relief=bk.RAISED)

    if penanda_fitur == 0 and penanda == 1:  # 0 berarti simple
        fu.tombol_naik.grid(row=2, column=2, pady=2)
        fu.tombol_turun.grid(row=3, column=2, pady=2)
        fu.format_posisi.pack(pady=1)
        fu.tulisan.pack(pady=1)
        fu.tulisan_jenis_gedung.pack(pady=5, padx=5)
        fu.tombol_pengubah_fitur.grid(row=2, column=3)
        fu.tombol_pengubah_fitur.configure(text="Fitur Komplex")
        fu.gambar_lantai.pack()

        fu.tombol_semua_lantai.grid_remove()
        fu.tombol_menghapus_lantai.grid_remove()
        fu.tombol_menambah_lantai.grid_remove()
        fu.tulisan_mengganti_gedung.grid_remove()
        fu.spinbox_gedung.grid_remove()
        fu.tombol_ubah.grid_remove()
        fu.background_gelap.pack_forget()
        fu.background_terang.pack_forget()

        bingkai_4.grid_remove()
        bingkai_6.grid_remove()

        penanda_fitur, penanda = 1, 0
    elif penanda_fitur == 1 and penanda == 1:  # 1 berarti komplex
        fu.tombol_semua_lantai.grid(row=3, column=3, padx=2, pady=2)
        fu.tombol_menghapus_lantai.grid(row=3, column=4, padx=2, pady=2)
        fu.tombol_menambah_lantai.grid(row=2, column=4, padx=2, pady=2)
        fu.tulisan_mengganti_gedung.grid(row=0, column=0, columnspan=2, pady=5, padx=5)
        fu.spinbox_gedung.grid(row=1, column=0, pady=5, padx=5)
        fu.tombol_ubah.grid(row=1, column=1, pady=2, padx=2)
        fu.tombol_pengubah_fitur.configure(text="Fitur Simple")
        fu.background_gelap.pack()
        fu.background_terang.pack()

        bingkai_4.grid(row=1, column=3, padx=5, pady=5)
        bingkai_6.grid(row=1, column=2, padx=5, pady=5)

        penanda_fitur, penanda = 0, 0

    bingkai_utama.place(rely=0.0, relx=0.0, x=0, y=0)
    bingkai_1.grid(row=0, column=1, padx=5, pady=5, columnspan=3)
    bingkai_2.grid(row=1, column=1, pady=5, padx=5)
    bingkai_3.grid(row=0, column=0, pady=5, padx=5)
    bingkai_5.grid(row=1, column=0, pady=5, padx=5)
    fu.nama_programmer.place(rely=1.0, relx=1.0, y=0, x=0, anchor=bk.SE)
    layar.mainloop()


class PembuatanLantaiBaru:
    nama_lantai_baru = bk.Entry(bingkai_1, bd=3, textvariable=input_lantai)  # bisa disatuin fungsinya: 1
    tombol_konfirmasi_1 = bk.Button(bingkai_1, text="Iya", command=lambda: plb.lantai_baru("IYA"))  #
    # bisa disatuin fungsinya: 2
    tombol_konfirmasi_2 = bk.Button(bingkai_1, text="Tidak", command=lambda: plb.lantai_baru("TIDAK"))  #
    # bisa disatuin fugnsinya: 3
    tombol_konfirmasi_3 = bk.Button(bingkai_1, text="Konfirmasi nama lantai",
                                    command=lambda: plb.menambah_lantai_atau_menutup(pilihan))  #
    # bisa disatuin fungsinya: 4
    tulisan_konfirmasi = bk.Label(bingkai_1, text="Apakah anda ingin membuat lantai baru?", bg="#c6f653")  #
    # bisa disatuin fungsinya: 5

    def __init__(self):
        pass

    @staticmethod
    def mulai():
        plb.tombol_konfirmasi_1.grid(row=1, column=1)  # ts_2 0 <
        plb.tombol_konfirmasi_2.grid(row=1, column=3)  # ts_3 0 <
        plb.tulisan_konfirmasi.grid(row=0, column=1, columnspan=3)  # ts_5 0 <

    @staticmethod
    def tambah_lantai():
        global penanda_batasan, susunan_lantai
        if penanda_batasan >= 6:
            susunan_lantai.append(plb.nama_lantai_baru.get())
        elif penanda_batasan <= -6:
            susunan_lantai.insert(0, plb.nama_lantai_baru.get())
        elif -5 <= penanda_batasan <= 5:
            susunan_lantai.insert(susunan_lantai.index(fu.spinbox_lantai.get()), plb.nama_lantai_baru.get())
        plb.nama_lantai_baru.delete(0, last=bk.END)
        penanda_batasan = 0
        layar.after(2100, plb.nama_lantai_baru.grid_remove())  # ts_1 1 <
        plb.tulisan_konfirmasi.grid_remove()  # ts_5 1 <
        plb.tombol_konfirmasi_3.grid_remove()  # ts_4 1 <
        fu.tombol_semua_lantai.configure(state=bk.NORMAL, relief=bk.GROOVE, text="Tekan untuk perbarui")
        fu.spinbox_lantai.configure(values=susunan_lantai)
        fu.spinbox_lantai.grid_remove()
        utama(0)

    @staticmethod
    def menambah_lantai_atau_menutup(keputusan):
        global penanda_batasan, pilihan
        if keputusan == "TAMBAH":
            plb.tambah_lantai()
        elif keputusan == "TUTUP":
            plb.tutup()
        elif keputusan == "TAMBAH" and -5 <= penanda_batasan <= 5:
            plb.tulisan_konfirmasi.configure(text="Pilih letak pembuatan lantai barunya")
            pilihan = "TAMBAH_ATUR"
        elif keputusan == "TAMBAH_ATUR":
            plb.tambah_lantai()

    @staticmethod
    def lantai_baru(konfirmasi):
        global susunan_lantai, pilihan, penanda_tampil, penanda_batasan
        fu.tombol_naik.configure(state=bk.DISABLED)
        fu.tombol_turun.configure(state=bk.DISABLED)
        posisi, penanda_tampil = 3, 0
        plb.tulisan_konfirmasi.grid(row=0, column=1, columnspan=3)  # ts_5 0 <
        plb.tombol_konfirmasi_1.grid_remove()  # ts_2 1 <
        plb.tombol_konfirmasi_2.grid_remove()  # ts_3 1 <
        plb.tombol_konfirmasi_3.configure(text="Konfirmasi nama lantai")
        plb.tulisan_konfirmasi.configure(text="Masukkan nama lantai yang ingin anda tambahkan:")
        plb.nama_lantai_baru.grid(row=1, column=0, columnspan=3)  # ts_1 0 <
        pilihan = "TAMBAH"
        plb.nama_lantai_baru.icursor(0)
        if konfirmasi == "TIDAK":
            penanda_tampil = 1
            plb.tombol_konfirmasi_3.configure(text="Tutup")
            pilihan = "TUTUP"
            posisi = 2
            plb.nama_lantai_baru.grid_remove()
            plb.tulisan_konfirmasi.configure(text="Baiklah")
        elif konfirmasi == "IYA" and -5 <= penanda_batasan <= 5:
            fu.spinbox_lantai.grid(row=5, column=2, pady=1, padx=1)
        plb.tombol_konfirmasi_3.grid(row=1, column=posisi)  # ts_4 0 <

        # utama()

    @staticmethod
    def tutup():
        global penanda_batasan
        penanda_batasan = 0
        plb.tulisan_konfirmasi.configure(text="Apakah anda ingin membuat lantai baru?")
        plb.tulisan_konfirmasi.grid_remove()  # ts_5 1 >
        plb.tombol_konfirmasi_3.grid_remove()  # ts_4 1 >
        utama(0)

    # batas class


plb = PembuatanLantaiBaru()


class FormatMultifungi:
    @staticmethod
    def format_dan_menambah_nama_lantai():
        tulisan_nama_lantai_ajaib = susunan_lantai[0]
        for counter_loop_gajelas in range(len(susunan_lantai[1:])):
            if counter_loop_gajelas % 5 == 0 and counter_loop_gajelas != 0:
                tulisan_nama_lantai_ajaib = tulisan_nama_lantai_ajaib + "\n"
            else:
                pass
            tulisan_nama_lantai_ajaib = tulisan_nama_lantai_ajaib + ", " + susunan_lantai[counter_loop_gajelas + 1]

        return tulisan_nama_lantai_ajaib

    @staticmethod
    def buka_jenis_gedung():
        global susunan_lantai, penanda_tampil, lantai, tulisan_ajaib
        fu.tulisan_jenis_gedung.configure(text="Tipe: " + fu.spinbox_gedung.get())
        susunan_lantai.clear()
        alamat_sementara = alamat + "/" + str(fu.spinbox_gedung.get()) + ".txt"
        with open(alamat_sementara, "r") as ganti:
            susunan_lantai = ganti.readlines()
            for i in range(len(susunan_lantai)):
                susunan_lantai[i] = susunan_lantai[i].replace("\n", "")
        lantai = susunan_lantai.index("G")
        tulisan_ajaib.set("Lantai G")
        if penanda_tampil == 1:
            fu.tombol_semua_lantai.configure(text="Tekan untuk perbarui")
            penanda_tampil = 0
        elif penanda_tampil != 1:
            pass
        return True

    @staticmethod
    def format_list_gedung():
        global lantai_pada_gedung
        for i in range(len(lantai_pada_gedung)):
            lantai_pada_gedung[i] = lantai_pada_gedung[i].replace(".txt", "")
        return lantai_pada_gedung

    @staticmethod
    def ganti_background():
        warna = penentu_background.get()
        if warna == "GELAP":
            layar.configure(bg="#2e2d2c")
            bingkai_utama.configure(bg="#383635")
            bingkai_1.configure(bg="#484645")
            bingkai_2.configure(bg="#484645")
            bingkai_3.configure(bg="#484645")
            bingkai_4.configure(bg="#484645")
            bingkai_5.configure(bg="#484645")
        elif warna == "TERANG":
            layar.configure(bg="#f0f0f0")
            bingkai_utama.configure(bg="#f0f0f0")
            bingkai_1.configure(bg="#ffe9cb")
            bingkai_2.configure(bg="#ffedb0")
            bingkai_3.configure(bg="#d5dfff")
            bingkai_4.configure(bg="#ffa97f")
            bingkai_5.configure(bg="#f0f0f0")


fm = FormatMultifungi()


class FungsiUtama:
    global susunan_lantai
    tombol_naik = bk.Button(bingkai_1, text="Naik 1 lantai",
                            command=lambda: naik_atau_turun("NAIK"), state=bk.NORMAL, relief=bk.RAISED, bg="#ddff92")
    tombol_turun = bk.Button(bingkai_1, text="Turun 1 lantai",
                             command=lambda: naik_atau_turun("TURUN"), state=bk.NORMAL, relief=bk.RAISED, bg="#ddff92")
    tulisan = bk.Label(bingkai_2, textvariable=tulisan_ajaib, bg="#ffc6b0", relief=bk.SUNKEN)
    format_posisi = bk.Label(bingkai_2, textvariable=format_posisi_ajaib, bg="#e9ffb0", relief=bk.RAISED)
    tombol_semua_lantai = bk.Button(bingkai_1, text="Tunjukkan semua lantai", state=bk.NORMAL,
                                    bg="#ffa952", relief=bk.GROOVE, command=lambda: tampilkan_lantai("TAMPIL"))

    tampilan_lantai_lantai = bk.Label(bingkai_1, text="Tidak ada apa-apa", relief=bk.RIDGE, bg="#fffb95")  #
    # bisa disatuin fungsinya: 6
    tombol_menghapus_lantai = bk.Button(bingkai_1, text="Tekan untuk menghapus lantai", state=bk.NORMAL,
                                        relief=bk.RAISED, bg="#ff2a3e", command=lambda: menghapus_lantai("HAPUS"))
    spinbox_lantai = bk.Spinbox(bingkai_1, values=susunan_lantai, textvariable=format_spinbox_ajaib, state=bk.NORMAL,
                                relief=bk.RAISED)
    tombol_menambah_lantai = bk.Button(bingkai_1, text="Tekan untuk menambah lantai", state=bk.NORMAL,
                                       relief=bk.RAISED, bg="#8bff62", command=lambda: plb.lantai_baru("IYA"))
    tulisan_jenis_gedung = bk.Label(bingkai_3, text="Tipe: Apartemen 1", bg="#fff5d5", relief=bk.GROOVE)
    tulisan_mengganti_gedung = bk.Label(bingkai_4, text="Tekan untuk memilih jenis gedung",
                                        bg="#ffec55", relief=bk.RIDGE)
    spinbox_gedung = bk.Spinbox(bingkai_4, values=fm.format_list_gedung(), textvariable=tulisan_gedung_ajaib,
                                bg="#ff6d00", relief=bk.SUNKEN)
    tombol_ubah = bk.Button(bingkai_4, text="Ubah", bg="#ffd27f", relief=bk.RAISED,
                            command=lambda: fm.buka_jenis_gedung())
    tombol_pengubah_fitur = bk.Button(bingkai_1, text="Fitur Komplex", bg="#e1ffaa",
                                      relief=bk.RAISED, command=lambda: utama(1))
    gambar_lantai = bk.Label(bingkai_5, image=gambar_lantai_gedung)
    nama_programmer = bk.Label(layar, text="Dibuat oleh Georgius Rama, Art oleh Clara Cinta   ",
                               font=("Times New Roman", 7), anchor=bk.SE)
    background_terang = bk.Radiobutton(bingkai_6, text="Gelap", variable=penentu_background,
                                       value="GELAP", command=fm.ganti_background, bg="#636363", relief=bk.RIDGE)
    background_gelap = bk.Radiobutton(bingkai_6, text="Terang", variable=penentu_background,
                                      value="TERANG", command=fm.ganti_background, bg="#636363", relief=bk.RIDGE)


fu = FungsiUtama()


def tampilkan_lantai(arahan):
    global penanda_tampil, susunan_lantai
    if arahan == "TAMPIL" and penanda_tampil == 0:
        penanda_tampil = 1
        fu.tampilan_lantai_lantai.configure(text=fm.format_dan_menambah_nama_lantai())
        fu.tombol_semua_lantai.configure(text="Tekan untuk sembunyikan")
        fu.tampilan_lantai_lantai.grid(row=4, column=3, padx=1, pady=1)  # ts_6 0 <
        # print(fu.spinbox_lantai.get())
        # fu.spinbox_lantai.grid_remove()
    elif arahan == "TAMPIL" and penanda_tampil != 0:
        fu.tampilan_lantai_lantai.grid_remove()  # ts_6 1 <
        penanda_tampil = 0
        fu.tombol_semua_lantai.configure(text="Tunjukkan semua lantai")
        # fu.spinbox_lantai.grid(row=5, column=2, pady=1, padx=1)
    return penanda_tampil


def menghapus_lantai(perintah):
    global penanda_tampil, penanda_hapus, susunan_lantai
    if perintah == "HAPUS" and penanda_hapus == 0:
        penanda_hapus = 1
        if penanda_tampil == 1:
            pass
        elif penanda_tampil != 1:
            fu.tampilan_lantai_lantai.configure(text=fm.format_dan_menambah_nama_lantai())
            fu.tombol_semua_lantai.configure(text="Tekan untuk perbarui")
            fu.tampilan_lantai_lantai.grid(row=4, column=3, padx=1, pady=1)  # ts_6 0 >
        plb.tulisan_konfirmasi.configure(text="Masukkan nama lantai yang ingin dihapus")
        plb.tulisan_konfirmasi.grid(row=0, column=1, columnspan=3)  # ts_5 0 >
        plb.nama_lantai_baru.grid(row=1, column=0, columnspan=3)  # ts_1 0 >
        fu.tombol_naik.configure(state=bk.DISABLED, relief=bk.FLAT)  # ada lagi groove dan ridged
        fu.tombol_turun.configure(state=bk.DISABLED, relief=bk.FLAT)
        fu.spinbox_lantai.configure(state=bk.DISABLED, relief=bk.FLAT)
        fu.tombol_menambah_lantai.configure(state=bk.DISABLED, relief=bk.FLAT)
        fu.tombol_semua_lantai.configure(state=bk.DISABLED, relief=bk.FLAT)
        fu.tombol_menghapus_lantai.configure(text="Konfirmasi untuk dihapus")
    elif perintah == "HAPUS" and penanda_hapus != 0:
        fu.tombol_menghapus_lantai.grid(row=3, column=4, padx=2, pady=2)
        nama_lantai_dihapus = plb.nama_lantai_baru.get()
        if nama_lantai_dihapus not in susunan_lantai[:]:
            plb.tulisan_konfirmasi.configure(text="Nama Lantai tersebut tidak ada!")
            plb.tulisan_konfirmasi.grid(row=0, column=1, columnspan=3)  # ts_5 0 >
            plb.nama_lantai_baru.delete(0, last=bk.END)
        elif nama_lantai_dihapus in susunan_lantai[:]:
            plb.tulisan_konfirmasi.configure(text="Lantai tersebut akan dihapus")
            plb.tulisan_konfirmasi.grid(row=0, column=1, columnspan=3)  # ts_5 0 >
            plb.nama_lantai_baru.delete(0, last=bk.END)
            plb.tulisan_konfirmasi.configure(text="Apakah anda ingin membuat lantai baru?")
            layar.after(1800, plb.tulisan_konfirmasi.grid_remove())  # ts_5 1 >
            fu.tombol_menghapus_lantai.configure(text="Tekan untuk menghapus lantai")
            fu.tombol_menghapus_lantai.grid(row=3, column=4, padx=2, pady=2)
            plb.nama_lantai_baru.grid_remove()  # ts_1 1 >
            susunan_lantai.remove(nama_lantai_dihapus)
            fu.tombol_semua_lantai.grid(row=3, column=3, padx=2, pady=2)
            fu.spinbox_lantai.configure(values=susunan_lantai)
            penanda_hapus = 0
            utama(0)

    return True


def lokasi_lantai(tempat):
    global lantai, penanda_batasan, susunan_lantai
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
    global lantai_berapa, lantai, susunan_lantai

    if penanda_batasan >= 6 or penanda_batasan <= -6:  # dengan batasan 6, memerlukan 7 kali pencetan tombol.
        # ya ga terlalu masalah sih
        fu.tombol_naik.configure(state=bk.DISABLED, relief=bk.FLAT)  # ada lagi groove dan ridged
        fu.tombol_turun.configure(state=bk.DISABLED, relief=bk.FLAT)
        fu.tombol_semua_lantai.configure(state=bk.DISABLED, relief=bk.FLAT)
        fu.tombol_menghapus_lantai.configure(state=bk.DISABLED, relief=bk.FLAT)
        plb.mulai()

    if tujuan == "NAIK":
        lantai = lantai + 1
    elif tujuan == "TURUN":
        lantai = lantai - 1
    lantai_berapa = "Lantai " + lokasi_lantai(lantai)
    tulisan_ajaib.set(lantai_berapa)

    # utama()


utama(1)

# batas
