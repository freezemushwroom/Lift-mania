import tkinter as bk  # kalo mau buat app make terminal dan namanya ada space ditulis pake ' '

# langkah berikutnya adalah memunculkan icon bitmap
# membuat gambar dari gedungnya, atau menggunakan paint trus diapain bisa lah
# dan memperbagus user interfacenya, mungkin warna, tekstur, dan menambah hiasan pada GUI
# update akan dilanjutkan saat udah ada internet lagi, yaitu senin-rabu besok

layar = bk.Tk()
layar.geometry("680x340")
layar.title("Lift Mania")
layar.iconbitmap("Ikon Lift Mania Asli.ico")
bingkai_1 = bk.LabelFrame(layar, text="Pengendali", bg="#ffe9cb", padx=10, pady=10, borderwidth=5, border=5)
bingkai_2 = bk.LabelFrame(layar, text="Tampilan Utama", bg="#ffedb0", padx=10, pady=10, borderwidth=5, border=5)
bingkai_3 = bk.LabelFrame(layar, text="Spesifikasi Bangungan", bg="#d5dfff", pady=10, padx=10, borderwidth=5, border=5)
tulisan_ajaib = bk.StringVar()
format_posisi_ajaib = bk.StringVar()
input_lantai = bk.StringVar()
format_spinbox_ajaib = bk.StringVar()
format_posisi_ajaib.set("Anda berada di ")
lantai_berapa = "Lantai G"
tulisan_ajaib.set("Lantai G")
format_lantai, pilihan = "Sekarang kita berada di lantai ", "TUTUP"
lantai, penanda_batasan, penanda_tampil, penanda_hapus = 4, 1, 0, 0
susunan_lantai = ["B3", "B2", "B1", "LG", "G", "UG", "1", "2", "3", "4", "5", "6", "7", "Rooftop"]  # total 14 lantai
urutan_lantai = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]  # mathcing dengan susunan lantainya
# ground di lantai ke 4 pada awalnya


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
        utama()

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
        fu.tombol_naik.grid_remove()
        fu.tombol_turun.grid_remove()
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
        utama()

    # batas class


plb = PembuatanLantaiBaru()


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
    tulisan_jenis_gedung = bk.Label(bingkai_3, text="Tipe: Apartemen", bg="#fff5d5", relief=bk.GROOVE)


fu = FungsiUtama()


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


fm = FormatMultifungi()


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
            utama()

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


def utama():
    global tulisan_ajaib, penanda_batasan

    fu.tombol_naik.configure(state=bk.NORMAL, relief=bk.RAISED)
    fu.tombol_turun.configure(state=bk.NORMAL, relief=bk.RAISED)
    fu.tombol_semua_lantai.configure(state=bk.NORMAL, relief=bk.GROOVE)
    fu.tombol_menghapus_lantai.configure(state=bk.NORMAL, relief=bk.RAISED)
    fu.spinbox_lantai.configure(state=bk.NORMAL, relief=bk.RAISED)
    fu.tombol_menambah_lantai.configure(state=bk.NORMAL, relief=bk.RAISED)

    fu.tombol_naik.grid(row=2, column=2, pady=2)
    fu.tombol_turun.grid(row=3, column=2, pady=2)
    fu.tombol_semua_lantai.grid(row=3, column=3, padx=2, pady=2)
    fu.tombol_menghapus_lantai.grid(row=3, column=4, padx=2, pady=2)
    fu.format_posisi.pack(pady=1)
    fu.tulisan.pack(pady=1)
    fu.tombol_menambah_lantai.grid(row=2, column=4, padx=2, pady=2)
    fu.tulisan_jenis_gedung.pack()

    bingkai_1.grid(row=0, column=1, padx=5, pady=5)
    bingkai_2.grid(row=1, column=1, pady=5, padx=5)
    bingkai_3.grid(row=0, column=0, pady=5, padx=5)
    layar.mainloop()


utama()

# batas
